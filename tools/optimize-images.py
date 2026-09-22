#!/usr/bin/env python3
"""Turn the full-size source photos into web-sized WebP + JPEG fallbacks.

Sources are never modified. Everything is written to assets/img/.
EXIF rotation is baked into the pixels here, because WebP does not carry it
and the photos come off the camera stored sideways.

    python3 tools/optimize-images.py ["../media/more content for landing page"]
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img"
DEFAULT_SRC = ROOT.parent / "media" / "more content for landing page"

# page name -> source file
PHOTOS = {
    "hero": "WhatsApp Image 2026-09-22 at 16.46.19.jpeg",   # standing before the temple at dawn
    "window": "WhatsApp Image 2026-09-22 at 16.46.22.jpeg",  # in the temple window
    "road": "DSC_9047.jpg",        # arms open, golden light, upright frame
    "open": "DSC_9046.jpg",        # arms open, wide frame
    "temple": "DSC_8999.JPG",      # from behind, facing the temple
    "reach": "DSC_9044.JPG",       # seated, arm raised
    "seated": "DSC_9041.jpg",      # seated, backlit
    "portrait": "DSC_9002.JPG",    # looking back at camera
    "speaking": "1728407623653.jpeg",  # Mastering Connections, Ball Janik
}
WIDTHS = (800, 1400, 2000)


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
            for width in WIDTHS:
                if width > im.width:
                    continue  # never upscale; the source is the ceiling
                height = round(im.height * width / im.width)
                resized = im.resize((width, height), Image.LANCZOS)
                resized.save(OUT / f"{name}-{width}.webp", "WEBP", quality=78, method=6)
                resized.save(OUT / f"{name}-{width}.jpg", "JPEG", quality=72,
                             optimize=True, progressive=True)
            made = [w for w in WIDTHS if w <= im.width]
            print(f"{name}: {im.width}x{im.height} -> {made}")

    print(f"done -> {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
