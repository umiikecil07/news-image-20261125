"""Drawing helpers: font loading, text wrapping and fitting.

Fonts ship in the repository under fonts/ so rendering is identical
anywhere the program runs. All helpers are pure functions of their
inputs, so the output image is deterministic.
"""

import os

from PIL import ImageFont

_HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(_HERE, "fonts")

SERIF = os.path.join(FONT_DIR, "DejaVuSerif.ttf")
SERIF_BOLD = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")

_SYSTEM_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts",
]


def _resolve(path):
    if os.path.exists(path):
        return path
    name = os.path.basename(path)
    for d in _SYSTEM_DIRS:
        cand = os.path.join(d, name)
        if os.path.exists(cand):
            return cand
    return path


def font(path, size):
    """Load a TrueType font at the given size."""
    return ImageFont.truetype(_resolve(path), size)


def text_width(draw, text, fnt):
    return draw.textlength(text, font=fnt)


def wrap_text(draw, text, fnt, max_width):
    """Greedy word wrap. Returns a list of lines that fit max_width."""
    words = text.split()
    if not words:
        return [""]
    lines = []
    current = words[0]
    for word in words[1:]:
        trial = current + " " + word
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def fit_lines(draw, text, fnt, max_width, max_lines):
    """Wrap text and report whether it fits in max_lines."""
    lines = wrap_text(draw, text, fnt, max_width)
    return lines, len(lines) <= max_lines


def fit_size(draw, text, path, start_size, max_width, min_size=8):
    """Largest font size (from start_size down) at which text fits."""
    size = start_size
    while size > min_size:
        fnt = font(path, size)
        if draw.textlength(text, font=fnt) <= max_width:
            return fnt
        size -= 1
    return font(path, min_size)


def centered(draw, y, text, fnt, fill, width, x0=0):
    """Draw text centred in [x0, x0+width] at baseline y."""
    w = draw.textlength(text, font=fnt)
    draw.text((x0 + (width - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def rule(draw, x0, y, x1, width, fill):
    """A solid horizontal rule."""
    draw.rectangle([x0, y, x1, y + width - 1], fill=fill)
