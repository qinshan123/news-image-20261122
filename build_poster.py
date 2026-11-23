#!/usr/bin/env python3
"""Build the 1024x1024 front-page poster for make.fun news-image-20261122.

Layout is data-driven: a masthead, a hero-art band, the lead story, a
2x2 grid of secondary stories and a navy ticker along the bottom.
Everything is drawn with Pillow from the STORIES table below, so swapping
in another day's news means editing data, not drawing code.
"""
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
HERO_FILE = os.path.join(
    HERE, "assets",
    "media-generation-news-hero-20261122-0-5912f9fb-f292-46da-bfab-0fe043e07a32.webp")
OUTPUT_FILE = os.path.join(HERE, "assets", "entry.png")

FONT_DIR = "/usr/share/fonts/truetype/noto"
SERIF_BLACK = os.path.join(FONT_DIR, "NotoSerif-Bold.ttf")
SANS_BLACK = os.path.join(FONT_DIR, "NotoSans-Bold.ttf")
SANS_PLAIN = os.path.join(FONT_DIR, "NotoSans-Regular.ttf")

PAGE = 1024
MARGIN = 40
CONTENT_W = PAGE - 2 * MARGIN
PAPER = (244, 239, 230)
BODY_INK = (24, 28, 38)
FADED_INK = (88, 94, 106)
ACCENT_RED = (176, 32, 32)
DEEP_NAVY = (15, 27, 51)
CARD_BG = (255, 255, 255)
CARD_EDGE = (198, 193, 183)

PAPER_NAME = "THE WORLD TODAY"
DATE_LINE = "SUNDAY  ·  22 NOVEMBER 2026  ·  THE DAY IN ONE PICTURE"

LEAD_HEADLINE = "COP31 TALKS COLLAPSE IN ANTALYA"
LEAD_SUMMARY = (
    "After a record 48 hours of overtime, nearly 200 nations leave "
    "T\u00fcrkiye with no deal: the EU and climate-vulnerable states "
    "reject a closing text with no fossil-fuel phase-out."
)

STORIES = [
    {
        "section": "MIDDLE EAST",
        "headline": "Iran strikes Bahrain, tankers hit",
        "body": ("Bahrain says an Iranian attack on a civilian industrial "
                 "site wounded two people; two tankers were struck near "
                 "the Strait of Hormuz."),
    },
    {
        "section": "LIBYA",
        "headline": "Russian warship ablaze at Benghazi",
        "body": ("Corvette Merkury caught fire after suspected Ukrainian "
                 "sea drones slipped past the port's defences. The UN "
                 "urges a probe."),
    },
    {
        "section": "MEXICO",
        "headline": "Cartel kingpin \u2018Chapo Isidro\u2019 taken",
        "body": ("FBI most-wanted Fausto Isidro Meza Flores is captured "
                 "in a deadly operation; burnt-out vehicles line the "
                 "roads of Sinaloa."),
    },
    {
        "section": "WASHINGTON",
        "headline": "Hackers breach FBI crime database",
        "body": ("An intrusion into the NCIC fingerprint and "
                 "wanted-persons system is confirmed; the Agriculture "
                 "Department is also hit."),
    },
]

TICKER_ITEMS = [
    "Poland confirms Russian Kh-101 missiles in its airspace",
    "Netanyahu\u2013Eisenkot talks end without a deal",
    "India and China wrap up border talks",
    "Liverpool rout United 4\u20130",
]


def load_font(path, size):
    return ImageFont.truetype(path, size)


def draw_centered(draw, text, top, font, fill, spacing=0):
    """Draw one line of text horizontally centred on the page."""
    if spacing:
        glyphs = [(ch, draw.textlength(ch, font=font)) for ch in text]
        total = sum(w for _, w in glyphs) + spacing * (len(glyphs) - 1)
        cursor = (PAGE - total) / 2
        for ch, w in glyphs:
            draw.text((cursor, top), ch, font=font, fill=fill)
            cursor += w + spacing
    else:
        width = draw.textlength(text, font=font)
        draw.text(((PAGE - width) / 2, top), text, font=font, fill=fill)


def paste_hero(page_img, top, height):
    """Centre-crop the generated cover art into the hero band."""
    art = Image.open(HERO_FILE).convert("RGB")
    scale = max(CONTENT_W / art.width, height / art.height)
    art = art.resize((round(art.width * scale), round(art.height * scale)),
                     Image.LANCZOS)
    left = (art.width - CONTENT_W) // 2
    upper = (art.height - height) // 2
    art = art.crop((left, upper, left + CONTENT_W, upper + height))
    page_img.paste(art, (MARGIN, top))
    frame = ImageDraw.Draw(page_img)
    frame.rectangle([MARGIN, top, MARGIN + CONTENT_W, top + height],
                    outline=BODY_INK, width=2)


def draw_story_card(draw, story, left, top, width, height):
    """One secondary story as a card with a navy header strip.

    The strip carries the section name in paper-white bold type; the
    headline sits under it in ink black and the body in soft grey,
    wrapped to the card's inner measure.
    """
    inner_x = left + 18
    draw.rectangle([left, top, left + width, top + height],
                   fill=CARD_BG, outline=CARD_EDGE, width=1)
    draw.rectangle([left, top, left + width, top + 30], fill=DEEP_NAVY)
    draw.text((inner_x, top + 5), story["section"],
              font=load_font(SANS_BLACK, 16), fill=(240, 240, 235))
    draw.text((inner_x, top + 42), story["headline"],
              font=load_font(SANS_BLACK, 22), fill=BODY_INK)
    line_y = top + 76
    for line in textwrap.wrap(story["body"], 47):
        draw.text((inner_x, line_y), line,
                  font=load_font(SANS_PLAIN, 18), fill=(40, 44, 54))
        line_y += 23


def main():
    page_img = Image.new("RGB", (PAGE, PAGE), PAPER)
    draw = ImageDraw.Draw(page_img)

    # Masthead block.
    draw_centered(draw, PAPER_NAME, 18, load_font(SERIF_BLACK, 66), BODY_INK)
    draw.line([(MARGIN, 104), (PAGE - MARGIN, 104)], fill=BODY_INK, width=3)
    draw_centered(draw, DATE_LINE, 112, load_font(SANS_BLACK, 21),
                  FADED_INK, spacing=2)
    draw.line([(MARGIN, 144), (PAGE - MARGIN, 144)], fill=BODY_INK, width=1)

    # Hero band, then the lead story.
    paste_hero(page_img, top=156, height=300)
    draw = ImageDraw.Draw(page_img)
    y = 470
    draw.text((MARGIN, y), LEAD_HEADLINE,
              font=load_font(SANS_BLACK, 47), fill=ACCENT_RED)
    y += 60
    for line in textwrap.wrap(LEAD_SUMMARY, 86):
        draw.text((MARGIN, y), line,
                  font=load_font(SANS_PLAIN, 22), fill=BODY_INK)
        y += 29

    # Secondary stories in a 2x2 grid.
    card_w, card_h = 464, 146
    grid_top = 640
    for index, story in enumerate(STORIES):
        card_left = MARGIN + (index % 2) * (card_w + 16)
        card_top = grid_top + (index // 2) * (card_h + 12)
        draw_story_card(draw, story, card_left, card_top, card_w, card_h)

    # Bottom ticker on a navy band.
    draw.rectangle([0, 966, PAGE, PAGE], fill=DEEP_NAVY)
    ticker_text = "ALSO TODAY  ·  " + "  ·  ".join(TICKER_ITEMS)
    ticker_font = load_font(SANS_BLACK, 17)
    line_y = 976
    for line in textwrap.wrap(ticker_text, 98)[:2]:
        draw_centered(draw, line, line_y, ticker_font, (240, 240, 235))
        line_y += 24

    page_img.save(OUTPUT_FILE, "PNG", optimize=True)
    print("poster written:", OUTPUT_FILE, os.path.getsize(OUTPUT_FILE))


if __name__ == "__main__":
    main()
