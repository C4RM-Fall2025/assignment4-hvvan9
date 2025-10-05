#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 17:03:16 2025

@author: vv_an9
"""

def getBondDuration(y, face, couponRate, m, ppy=1):
    y_per = y / ppy
    n = int(m * ppy)
    c = face * couponRate / ppy

    price = 0.0
    weighted_pv_sum = 0.0

    for t in range(1, n + 1):
        cf = c if t < n else c + face
        df = (1 + y_per) ** (-t)
        pvcf = cf * df
        price += pvcf
        weighted_pv_sum += t * pvcf

    macaulay_duration_years = (weighted_pv_sum / price) / ppy
    return macaulay_duration_years

y = 0.03
face = 2_000_000
couponRate = 0.04
m = 10

duration = getBondDuration(y, face, couponRate, m, ppy=1)
print(f"Duration = {duration:.3f} years")
