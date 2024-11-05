# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:26:53 2024

@author: koos
"""

def estimate_mrt(air_temp, wind_speed, solar_radiation=800):
    """
    Simplified estimation of Mean Radiant Temperature (MRT)
    Uses a basic calculation based on air temperature and solar radiation
    """
    # Basic estimation: MRT is typically higher than air temperature during day
    # due to solar radiation, and close to air temperature at night
    solar_effect = solar_radiation / 1000  # Normalize solar radiation effect
    wind_cooling = math.log(wind_speed + 1) * 0.5  # Wind has a cooling effect
    
    # MRT estimation: air temperature plus solar effect, reduced by wind
    mrt = air_temp + (solar_effect * 5) - wind_cooling
    
    return mrt