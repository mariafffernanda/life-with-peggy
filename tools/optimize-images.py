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
    "hero": "DSC_9065.JPG",        # standing before the temple, wide
    "reach": "DSC_9044.JPG",       # seated, arm raised, open sky
    "portrait": "DSC_9002.JPG",    # looking back at camera
    "seated": "DSC_9041.jpg",      # seated, backlit
    "open": "DSC_9046.jpg",        # arms open, walking
    "temple": "DSC_8999.JPG",      # from behind, facing the temple
    "speaking": "1728407623653.jpeg",  # Mastering Connections, Ball Janik
}
WIDTHS = (800, 1400, 2000)

# Square crops for the social grid placeholder, centred on the frame.
SQUARES = {
    "social-1": "DSC_9002.JPG",
    "social-2": "1728407623653.jpeg",
    "social-3": "DSC_9046.jpg",
    "social-4": "DSC_9041.jpg",
    "social-5": "DSC_8999.JPG",
    "social-6": "DSC_9044.JPG",
}
SQUARE_SIZE = 700

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
                height = round(im.height * width / im.width)
                resized = im.resize((width, height), Image.LANCZOS)
                resized.save(OUT / f"{name}-{width}.webp", "WEBP", quality=78, method=6)
                resized.save(OUT / f"{name}-{width}.jpg", "JPEG", quality=72,
                             optimize=True, progressive=True)
            print(f"{name}: {im.width}x{im.height} -> {', '.join(map(str, WIDTHS))}")

    for name, filename in SQUARES.items():
        path = src_dir / filename
        if not path.is_file():
            print(f"missing: {path}", file=sys.stderr)
            return 1
        with Image.open(path) as im:
            im = ImageOps.exif_transpose(im).convert("RGB")
            square = ImageOps.fit(im, (SQUARE_SIZE, SQUARE_SIZE),
                                  Image.LANCZOS, centering=(0.5, 0.38))
            square.save(OUT / f"{name}.webp", "WEBP", quality=76, method=6)
            square.save(OUT / f"{name}.jpg", "JPEG", quality=70, optimize=True)
    print(f"squares: {len(SQUARES)} at {SQUARE_SIZE}px")
    print(f"done -> {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
