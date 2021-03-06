import pickle
from fractions import Fraction

conversionRates = {
    "tsp_tsp": (1 / 1),
    "tbsp_tsp": (3 / 1),
    "cup_tsp": (48 / 1),
    "oz_tsp": (6 / 1),
    "pt_tsp": (96 / 1),
    "qt_tsp": (192 / 1),
    "gal_tsp": (768 / 1),
    "lb_tsp": (96 / 1),
    "tsp_tbsp": (1 / 3),
    "tbsp_tbsp": (1 / 1),
    "cup_tbsp": (16 / 1),
    "oz_tbsp": (2 / 1),
    "pt_tbsp": (32 / 1),
    "qt_tbsp": (64 / 1),
    "gal_tbsp": (256 / 1),
    "lb_tbsp": (32 / 1),
    "tsp_cup": (1 / 48),
    "tbsp_cup": (1 / 16),
    "cup_cup": (1 / 1),
    "oz_cup": (1 / 8),
    "pt_cup": (2 / 1),
    "qt_cup": (4 / 1),
    "gal_cup": (16 / 1),
    "lb_cup": (32 / 1),
    "tsp_oz": (1 / 6),
    "tbsp_oz": (1 / 2),
    "cup_oz": (8 / 1),
    "oz_oz": (1 / 1),
    "pt_oz": (16 / 1),
    "qt_oz": (32 / 1),
    "gal_oz": (128 / 1),
    "lb_oz": (16 / 1),
    "tsp_pt": (1 / 96),
    "tbsp_pt": (1 / 32),
    "cup_pt": (1 / 2),
    "oz_pt": (1 / 16),
    "pt_pt": (1 / 1),
    "qt_pt": (2 / 1),
    "gal_pt": (8 / 1),
    "lb_pt": (1 / 1),
    "tsp_qt": (1 / 192),
    "tbsp_qt": (1 / 64),
    "cup_qt": (1 / 4),
    "oz_qt": (1 / 32),
    "pt_qt": (1 / 2),
    "qt_qt": (1 / 1),
    "gal_qt": (4 / 1),
    "lb_qt": (1 / 2),
    "tsp_gal": (1 / 768),
    "tbsp_gal": (1 / 256),
    "cup_gal": (1 / 16),
    "oz_gal": (1 / 128),
    "pt_gal": (1 / 8),
    "qt_gal": (1 / 4),
    "gal_gal": (1 / 1),
    "lb_gal": (1 / 8),
    "tsp_lb": (1 / 96),
    "tbsp_lb": (1 / 32),
    "cup_lb": (1 / 2),
    "oz_lb": (1 / 16),
    "pt_lb": (1 / 1),
    "qt_lb": (2 / 1),
    "gal_lb": (8 / 1),
    "lb_lb": (1 / 1),
}


def convert(conversion, amount):
    return conversionRates[conversion] * amount


# print(Fraction(convert("oz_lb", 16)).limit_denominator())
# print(Fraction(convert("tsp_tbsp", 5)).limit_denominator())
lst = [1, 2, 3]
print(lst)
lst = lst + [4, 5, 6]
print(lst)
