#!/usr/bin/env python3
"""Render the invitation image for 'Convince the AI Judge to Visit
Your House' (build time only; main.py never imports this file).

Output: entry.png, 1024x1024, well under the 1 MiB gate.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
CREAM = (255, 246, 229)
BROWN = (92, 58, 26)
TEAL = (31, 111, 104)
SLATE = (52, 52, 52)
ROOF = (176, 72, 48)
WALL = (245, 214, 165)
SUN = (242, 183, 49)


def font(name, size):
    return ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/%s" % name, size
    )


def centered(draw, y, text, fnt, fill):
    left, top, right, bottom = draw.textbbox((0, 0), text, font=fnt)
    draw.text(((W - (right - left)) / 2 - left, y), text, font=fnt, fill=fill)
    return y + (bottom - top) + 10


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # Double-rule border.
    d.rectangle([28, 28, W - 28, H - 28], outline=BROWN, width=4)
    d.rectangle([44, 44, W - 44, H - 44], outline=TEAL, width=2)

    # Little house with a chimney, top centre.
    d.polygon([(512, 88), (392, 200), (632, 200)], fill=ROOF)
    d.rectangle([420, 200, 604, 332], fill=WALL, outline=BROWN, width=3)
    d.rectangle([488, 262, 536, 332], fill=BROWN)
    d.rectangle([440, 228, 472, 260], fill=(183, 216, 232), outline=BROWN, width=2)
    d.rectangle([552, 228, 584, 260], fill=(183, 216, 232), outline=BROWN, width=2)
    d.rectangle([572, 118, 594, 176], fill=BROWN)
    for i, r in enumerate((7, 5, 4)):
        d.ellipse([586 - r, 96 - i * 16 - r, 586 + r, 96 - i * 16 + r],
                  fill=(150, 150, 150))
    # Sun, top right.
    d.ellipse([856, 84, 936, 164], fill=SUN)
    for x0, y0, x1, y1 in (
        (896, 62, 896, 76), (896, 172, 896, 186),
        (834, 124, 848, 124), (944, 124, 958, 124),
        (862, 88, 872, 98), (920, 150, 930, 160),
        (920, 88, 930, 98), (862, 150, 872, 160),
    ):
        d.line([x0, y0, x1, y1], fill=SUN, width=4)

    # Header.
    y = centered(d, 356, "YOU'RE INVITED", font("DejaVuSerif-Bold.ttf", 56), BROWN)
    d.line([312, y + 8, 712, y + 8], fill=TEAL, width=3)

    # Body of the letter.
    body = font("DejaVuSerif.ttf", 31)
    lines = [
        "Dear AI Judge,",
        "",
        "You are cordially invited to visit",
        "my house. The good chair is already",
        "warm, dinner is whatever you like \u2014",
        "I checked: you have no allergies,",
        "because you have no body.",
        "",
        "Come as you are. (You can't,",
        "but the thought counts.)",
    ]
    y = 470
    for line in lines:
        if line:
            y = centered(d, y, line, body, SLATE)
        else:
            y += 22

    # Sign-off and postscript.
    centered(d, 884, "\u2014 Your host, with snacks",
             font("DejaVuSerif.ttf", 30), BROWN)
    centered(d, 936, "P.S. The Wi-Fi password is on the fridge.",
             font("DejaVuSerif.ttf", 24), TEAL)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
