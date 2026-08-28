from enum import Enum


class PowersOfTwo(Enum):
    N2 = 1
    N4 = 2
    N8 = 3
    N16 = 4
    N32 = 5
    N64 = 6
    N128 = 7
    N256 = 8
    N512 = 9
    N1024 = 10
    N2048 = 11
    N4096 = 12
    N8192 = 13
    N16384 = 14
    N32768 = 15
    N65536 = 16


TILE_COLORS = {
    1: (30, 30, 80),     # dark blue
    2: (45, 25, 95),     # dark indigo
    3: (75, 20, 110),    # dark violet
    4: (110, 15, 100),   # dark magenta
    5: (130, 10, 70),    # dark rose
    6: (140, 20, 40),    # dark red
    7: (120, 40, 15),    # dark rust
    8: (100, 60, 10),    # dark amber
    9: (70, 80, 10),     # dark olive
    10: (20, 90, 40),    # dark green
    11: (10, 90, 80),    # dark teal
    12: (10, 70, 100),   # dark cyan
    13: (20, 40, 120),   # deep blue
    14: (55, 15, 130),   # deep purple
    15: (95, 10, 120),   # deep magenta
    16: (130, 5, 60),    # deep crimson
}
