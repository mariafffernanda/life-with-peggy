#!/usr/bin/env python3
"""Turn the full-size source photos into web-sized WebP + JPEG fallbacks.

Sources are never modified. Everything is written to assets/img/.
EXIF rotation is baked into the pixels here, because WebP does not carry it
and the photos come off the camera stored sideways.

    python3 tools/optimize-images.py ["../media"]
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img"
DEFAULT_SRC = ROOT.parent / "media"

# page name -> source file, relative to ../media/
LANDING = "more content for landing page/"
MAGIA = "Magia33 Content Sep 18/Imagenes Landing/"
PHOTOS = {
    "hero": LANDING + "WhatsApp Image 2026-09-22 at 16.46.19.jpeg",   # standing before the temple at dawn
    "window": LANDING + "WhatsApp Image 2026-09-22 at 16.46.22.jpeg",  # in the temple window
    "open": LANDING + "DSC_9046.jpg",        # arms open, wide frame (DSC_9047 is the same moment; never use both)
    "speaking": LANDING + "1728407623653.jpeg",  # Mastering Connections
    "venue": LANDING + "1698155008820.jpeg",     # ballroom of professionals, In organizations
    "circle": MAGIA + "CASA MAGIA 33-52.jpg",    # the circle at Magia 33, With individuals
    "dawn": LANDING + "DSC_9041.jpg",            # seated on the stone at dawn, the method
}
WIDTHS = (800, 1400, 2000)
BUDGET = 150 * 1024  # bytes per file


def save_within_budget(im, path, fmt, quality, **opts):
    """Step the quality down until the file fits the budget, floor 50."""
    while True:
        im.save(path, fmt, quality=quality, **opts)
        if path.stat().st_size <= BUDGET or quality <= 50:
            return quality
        quality -= 4


def main() -> int:
    src_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SRC
    if not src_dir.is_dir():
        print(f"source folder not found: {src_dir}", file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)

    for name, filename in PHOTOS.items():
        path = src_dir / filename
        if not path.is_file():
            print(f"missing: {path}", file=sys.stderr)
            return 1
        with Image.open(path) as im:
            im = ImageOps.exif_transpose(im).convert("RGB")
            # never upscale; a source too small for the 1400 size is also
            # written at its own width, so phones get every pixel there is
            widths = [w for w in WIDTHS if w <= im.width]
            if im.width < 1400 and im.width not in widths:
                widths.append(im.width)
            for width in widths:
                height = round(im.height * width / im.width)
                resized = im.resize((width, height), Image.LANCZOS)
                webp, jpg = OUT / f"{name}-{width}.webp", OUT / f"{name}-{width}.jpg"
                save_within_budget(resized, webp, "WEBP", 78, method=6)
                save_within_budget(resized, jpg, "JPEG", 72, optimize=True, progressive=True)
                if width not in WIDTHS and max(webp.stat().st_size, jpg.stat().st_size) > BUDGET:
                    webp.unlink()  # the extra size is optional; drop it rather than ship it heavy
                    jpg.unlink()
                    widths.remove(width)
            print(f"{name}: {im.width}x{im.height} -> {widths}")

    print(f"done -> {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
