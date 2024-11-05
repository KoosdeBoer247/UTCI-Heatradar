# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:26:53 2024

@author: koos
"""

def wet_bulb_tw(t, rh):
    a = t * atan(0.151977 * (rh + 8.313659) ** 0.5)
    b = atan(t + rh) - atan(rh - 1.676331)
    c = 0.00391838 * rh ** (1.5) * atan(0.023101 * rh)
    d = -4.686035
    tw = a + b + c + d
    return tw
