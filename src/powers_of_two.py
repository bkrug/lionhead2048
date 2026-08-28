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


TILE_COLORS: dict[int, tuple[float, float, float]] = {
    1: (0.1176, 0.1176, 0.3137),   # dark blue
    2: (0.1765, 0.0980, 0.3725),   # dark indigo
    3: (0.2941, 0.0784, 0.4314),   # dark violet
    4: (0.4314, 0.0588, 0.3922),   # dark magenta
    5: (0.5098, 0.0392, 0.2745),   # dark rose
    6: (0.5490, 0.0784, 0.1569),   # dark red
    7: (0.4706, 0.1569, 0.0588),   # dark rust
    8: (0.3922, 0.2353, 0.0392),   # dark amber
    9: (0.2745, 0.3137, 0.0392),   # dark olive
    10: (0.0784, 0.3529, 0.1569),  # dark green
    11: (0.0392, 0.3529, 0.3137),  # dark teal
    12: (0.0392, 0.2745, 0.3922),  # dark cyan
    13: (0.0784, 0.1569, 0.4706),  # deep blue
    14: (0.2157, 0.0588, 0.5098),  # deep purple
    15: (0.3725, 0.0392, 0.4706),  # deep magenta
    16: (0.5098, 0.0196, 0.2353),  # deep crimson
}
