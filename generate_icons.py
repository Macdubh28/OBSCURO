import os
from PIL import Image, ImageDraw, ImageFont
os.makedirs("icons", exist_ok=True)
def create_icon(size):
    img = Image.new("RGB", (size, size), color="#0a0f1e")
    draw = ImageDraw.Draw(img)

    # Cercle acier subtil
    margin = size * 0.08
    draw.ellipse(
        [margin, margin, size - margin, size - margin],
        outline="#1a3a6e",
        width=max(2, size // 60)
    )

    # Lettre O centrale — Cinzel-style
    font_size = int(size * 0.52)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        font = ImageFont.load_default()

    text = "O"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (size - tw) // 2
    y = (size - th) // 2 - size // 20

    draw.text((x, y), text, fill="#5b8fd4", font=font)

    # Trait bas
    line_y = size * 0.78
    line_x1 = size * 0.32
    line_x2 = size * 0.68
    draw.line([line_x1, line_y, line_x2, line_y], fill="#1a3a6e", width=max(1, size // 80))

    img.save(f"icons/icon-{size}.png")
    print(f"icon-{size}.png créé")
create_icon(192)
create_icon(512)
print("Icônes OBSCURO générées.")
