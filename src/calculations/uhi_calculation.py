# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:26:53 2024

@author: koos
"""

def calculate_uhi(city_population):
    if city_population <= 0:
        raise ValueError("City population size must be greater than zero.")
    uhi = 2.01 * math.log10(city_population) - 7.06
    return max(uhi, 0)
