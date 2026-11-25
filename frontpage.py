"""Compose the front page: a 1024x1024 newspaper front page.

Layout (all coordinates in pixels, canvas 1024x1024):
  dateline row, masthead, double rule, lead kicker + headline + summary,
  index-moves bar chart, navy markets strip, "More from the day" grid
  (2 columns x 3 rows), red ticker band, footer.

Every text block is wrapped and shrunk to fit its box, so nothing
overflows. The drawing is a pure function of stories.py, so two runs
produce byte-identical PNG output.
"""

import os

from PIL import Image, ImageDraw

import stories
from toolkit import (
    SANS,
    SANS_BOLD,
    SERIF,
    SERIF_BOLD,
    centered,
    fit_size,
    font,
    rule,
    wrap_text,
)

W = 1024
H = 1024
MARGIN = 36
CONTENT = W - 2 * MARGIN  # 952

PAPER = (248, 244, 236)
CARD = (255, 252, 246)
INK = (25, 25, 25)
BODY_INK = (48, 46, 43)
RED = (143, 29, 33)
NAVY = (31, 58, 95)
GRAY = (107, 103, 94)
GREEN = (46, 125, 50)
CARD_BORDER = (214, 206, 190)


def _fit_wrapped(draw, text, path, start_size, max_width, max_lines,
                 min_size=10):
    """Wrap text, shrinking the font until it fits in max_lines."""
    size = start_size
    while size > min_size:
        fnt = font(path, size)
        lines = wrap_text(draw, text, fnt, max_width)
        if len(lines) <= max_lines:
            return fnt, lines
        size -= 1
    fnt = font(path, min_size)
    return fnt, wrap_text(draw, text, fnt, max_width)


def _draw_dateline(draw):
    fnt = font(SANS_BOLD, 15)
    centered(draw, 16, stories.DATE_LINE, fnt, INK, W)
    small = font(SANS_BOLD, 13)
    draw.text((MARGIN, 18), "No. 329", font=small, fill=GRAY)
    right = "ONE PICTURE OF THE DAY"
    w = draw.textlength(right, font=small)
    draw.text((W - MARGIN - w, 18), right, font=small, fill=GRAY)


def _draw_masthead(draw):
    fnt = font(SERIF_BOLD, 62)
    centered(draw, 34, stories.MASTHEAD, fnt, INK, W)
    rule(draw, MARGIN, 114, W - MARGIN, 3, INK)
    rule(draw, MARGIN, 119, W - MARGIN, 1, INK)


def _draw_lead(draw):
    kicker = font(SANS_BOLD, 14)
    draw.text((MARGIN, 128), stories.LEAD_KICKER, font=kicker, fill=RED)
    head = font(SERIF_BOLD, 40)
    y = 146
    for line in stories.LEAD_HEADLINE:
        draw.text((MARGIN, y), line, font=head, fill=INK)
        y += 48
    body = font(SANS, 19)
    lines = wrap_text(draw, stories.LEAD_SUMMARY, body, CONTENT)
    y = 250
    for line in lines:
        draw.text((MARGIN, y), line, font=body, fill=BODY_INK)
        y += 23
    return y


def _draw_chart(draw, y0):
    label = font(SANS_BOLD, 12)
    draw.text((MARGIN, y0), "INDEX MOVES, % ON THE DAY",
              font=label, fill=GRAY)
    zero_x = 520
    scale = 30.0  # pixels per percentage point
    lab = font(SANS_BOLD, 14)
    val = font(SANS_BOLD, 13)
    y = y0 + 18
    for name, pct in stories.MARKET_BARS:
        nw = draw.textlength(name, font=lab)
        draw.text((170 - nw, y - 1), name, font=lab, fill=INK)
        width = abs(pct) * scale
        if pct < 0:
            draw.rectangle([zero_x - width, y, zero_x, y + 12], fill=RED)
            text = "%.1f%%" % pct
            tw = draw.textlength(text, font=val)
            draw.text((zero_x - width - 6 - tw, y - 1), text,
                      font=val, fill=RED)
        else:
            draw.rectangle([zero_x, y, zero_x + width, y + 12], fill=GREEN)
            text = "+%.1f%%" % pct
            draw.text((zero_x + width + 6, y - 1), text,
                      font=val, fill=GREEN)
        y += 15
    rule(draw, zero_x, y0 + 16, zero_x, y - y0 - 16, GRAY)
    return y


def _draw_markets_strip(draw, y0):
    draw.rectangle([MARGIN, y0, W - MARGIN, y0 + 44], fill=NAVY)
    fnt, lines = _fit_wrapped(draw, stories.MARKETS_STRIP, SANS_BOLD, 15,
                              CONTENT - 24, 2)
    y = y0 + 4
    for line in lines:
        centered(draw, y, line, fnt, (255, 255, 255), CONTENT, MARGIN)
        y += 20
    return y0 + 44


def _draw_card(draw, x, y, w, h, kicker, headline, body):
    draw.rectangle([x, y, x + w, y + h], fill=CARD, outline=CARD_BORDER)
    inner = w - 24
    kx = x + 12
    ky = y + 11
    kf = font(SANS_BOLD, 13)
    draw.text((kx, ky), kicker, font=kf, fill=RED)
    hf, hlines = _fit_wrapped(draw, headline, SERIF_BOLD, 19, inner, 2)
    hy = ky + 20
    for line in hlines:
        draw.text((kx, hy), line, font=hf, fill=INK)
        hy += 23
    bf, blines = _fit_wrapped(draw, body, SANS, 14, inner, 2)
    by = hy + 4
    for line in blines:
        draw.text((kx, by), line, font=bf, fill=BODY_INK)
        by += 17


def _draw_grid(draw, y0):
    label = font(SANS_BOLD, 13)
    draw.text((MARGIN, y0), stories.SECTION_LABEL, font=label, fill=RED)
    rule(draw, MARGIN, y0 + 18, W - MARGIN, 1, INK)
    gap = 16
    card_w = (CONTENT - gap) // 2
    card_h = 126
    gy = y0 + 26
    for row in range(3):
        for col in range(2):
            idx = row * 2 + col
            kicker, headline, body = stories.CARDS[idx]
            x = MARGIN + col * (card_w + gap)
            y = gy + row * (card_h + 9)
            _draw_card(draw, x, y, card_w, card_h, kicker, headline, body)
    return gy + 3 * card_h + 2 * 9


def _draw_ticker(draw, y0):
    draw.rectangle([MARGIN, y0, W - MARGIN, y0 + 50], fill=RED)
    text = "  •  ".join(stories.TICKER)
    fnt, lines = _fit_wrapped(draw, text, SANS_BOLD, 15, CONTENT - 28, 2,
                              min_size=11)
    y = y0 + 6
    for line in lines:
        centered(draw, y, line, fnt, (255, 255, 255), CONTENT, MARGIN)
        y += 20
    return y0 + 50


def _draw_footer(draw, y0):
    fnt = font(SANS, 13)
    centered(draw, y0, stories.FOOTER, fnt, GRAY, W)


def build_page():
    """Render the full front page and return a PIL Image."""
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    _draw_dateline(draw)
    _draw_masthead(draw)
    _draw_lead(draw)
    chart_end = _draw_chart(draw, 326)
    strip_end = _draw_markets_strip(draw, 444)
    grid_end = _draw_grid(draw, 496)
    ticker_end = _draw_ticker(draw, 926)
    _draw_footer(draw, 984)
    return img
