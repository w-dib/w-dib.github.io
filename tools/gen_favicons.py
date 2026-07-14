#!/usr/bin/env python3
"""Generate the full Chirpy 7.x favicon set from the site avatar (Walid's headshot)."""
import base64
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
FAV = ROOT / "assets" / "img" / "favicons"
SRC = FAV / "android-chrome-512x512.png"

src = Image.open(SRC).convert("RGBA")
# Ensure square (center-crop just in case)
w, h = src.size
side = min(w, h)
src = src.crop(((w - side) // 2, (h - side) // 2, (w - side) // 2 + side, (h - side) // 2 + side))


def resized(size):
    return src.resize((size, size), Image.LANCZOS)


# PNG raster icons referenced by Chirpy 7.x
resized(96).save(FAV / "favicon-96x96.png")
resized(180).save(FAV / "apple-touch-icon.png")
resized(192).save(FAV / "web-app-manifest-192x192.png")
resized(512).save(FAV / "web-app-manifest-512x512.png")

# Multi-resolution .ico
src.save(FAV / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

# SVG wrapper embedding the 192px PNG so svg-preferring browsers show the photo
png_bytes = (FAV / "web-app-manifest-192x192.png").read_bytes()
b64 = base64.b64encode(png_bytes).decode("ascii")
svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" '
    'viewBox="0 0 512 512">'
    f'<image width="512" height="512" href="data:image/png;base64,{b64}"/>'
    "</svg>\n"
)
(FAV / "favicon.svg").write_text(svg)

print("Favicons generated:")
for f in sorted(FAV.iterdir()):
    print(f"  {f.name}: {f.stat().st_size} bytes")
