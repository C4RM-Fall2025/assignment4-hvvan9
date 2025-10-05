#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 17:26:22 2025

@author: vv_an9
"""

def getBondPrice_E(face, couponRate, m, yc):
    
    coupon = face * couponRate   # annual coupon
    bondPrice = 0.0

    for t in range(1, m + 1):
        # cash flow: coupon each year, plus face at maturity
        cf = coupon if t < m else coupon + face
        # discount factor for year t using yc[t-1]
        df = 1 / ((1 + yc[t - 1]) ** t)
        bondPrice += cf * df

    return bondPrice

yc = [0.010, 0.015, 0.020, 0.025, 0.030]   # spot rates for years 1–5
face = 2000000
couponRate = 0.04
m = 5

price = getBondPrice_E(face, couponRate, m, yc)
print(f"Bond Price = ${price:,.2f}")
