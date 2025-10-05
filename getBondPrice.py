#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 17:48:33 2025

@author: vv_an9
"""

def getBondPrice(y, face, couponRate, m, ppy=1):
    
    y_per = y / ppy
    n = int(m * ppy)
    c = face * couponRate / ppy

    price = 0.0
    for t in range(1, n + 1):
        # last payment includes face value
        cf = c if t < n else c + face
        df = (1 + y_per) ** (-t)
        price += cf * df

    return price

