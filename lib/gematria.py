"""
    GEMATRIA Alphabet

"""

from __future__ import annotations
import math

class Gematria(object):
    """GEMATRIA class"""

    def __init__(self):
        self.gematriaprimus = (
            (" ", " ", 0),
            (u"ᚠ", "f", 2),
            (u"ᚢ", "v", 3),
            (u"ᚢ", "u", 3),
            (u"ᚦ", "T", 5),  # th
            (u"ᚩ", "o", 7),
            (u"ᚱ", "r", 11),
            (u"ᚳ", "k", 13),
            (u"ᚳ", "c", 13),
            (u"ᚷ", "g", 17),
            (u"ᚹ", "w", 19),
            (u"ᚻ", "h", 23),
            (u"ᚾ", "n", 29),
            (u"ᛁ", "i", 31),
            (u"ᛄ", "j", 37),
            (u"ᛇ", "E", 41),  # eo
            (u"ᛈ", "p", 43),
            (u"ᛉ", "x", 47),
            (u"ᛋ", "z", 53),
            (u"ᛋ", "s", 53),
            (u"ᛏ", "t", 59),
            (u"ᛒ", "b", 61),
            (u"ᛖ", "e", 67),
            (u"ᛗ", "m", 71),
            (u"ᛚ", "l", 73),
            (u"ᛝ", "G", 79),  # ing
            (u"ᛝ", "G", 79),  # ng
            (u"ᛟ", "O", 83),  # oe
            (u"ᛞ", "d", 89),
            (u"ᚪ", "a", 97),
            (u"ᚫ", "A", 101),  # ae
            (u"ᚣ", "y", 103),
            (u"ᛡ", "I", 107),  # ia
            (u"ᛡ", "I", 107),  # io
            (u"ᛠ", "X", 109),  # ea
        )
        self.latsimple = (
            ("T", "th"),
            ("E", "eo"),
            ("G", "ing"),
            ("G", "ng"),
            ("O", "oe"),
            ("A", "ae"),
            ("I", "io"),
            ("I", "ia"),
            ("X", "ea"),
        )

    # algorithm taken from here: https://pastebin.com/6v1XC1kV
    def gem_map(self, x, src, dest):
        m = {p[src]: p[dest] for p in self.gematriaprimus}
        return [m[c] if c in m else c for c in x]

    def lat_to_sim(self, x):
        x = x.lower().replace("qu", "kw").replace("q", "k")
        for sim in self.latsimple:
            x = x.replace(sim[1], sim[0])
        return x

    def sim_to_lat(self, x):
        for sim in self.latsimple:
            x = x.replace(sim[0], sim[1])
        return x

    def run_to_lat(self, x):
        return self.sim_to_lat("".join(self.gem_map(x, 0, 1)))

    def run_to_num(self, x):
        return self.gem_map(x, 0, 2)

    def lat_to_run(self, x):
        return "".join(self.gem_map(self.lat_to_sim(x), 1, 0))

    def lat_to_num(self, x):
        # strip non alpha chars when converting to num
        x = "".join([c for c in x if c.isalpha() or c == " "])
        return self.gem_map(self.lat_to_sim(x), 1, 2)

    def num_to_run(self, x):
        return self.gem_map(x, 2, 0)

    def num_to_lat(self, x):
        return self.sim_to_lat("".join(self.gem_map(x, 2, 1)))
