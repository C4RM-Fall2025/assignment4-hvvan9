#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 17:30:21 2025

@author: vv_an9
"""

def getBondPrice_Z(face, couponRate, times, yc):
    
    if len(times) != len(yc):
        raise ValueError("times and yc must have the same length")

    coupon = face * couponRate          
    T = max(times)                      
    price = 0.0

    for t, r in zip(times, yc):
        cf = coupon if t < T else coupon + face   
        df = (1 + r) ** (-t)                       
        price += cf * df

    return price

yc = [0.010, 0.015, 0.020, 0.025, 0.030]
times = [1, 1.5, 3, 4, 7]
face = 2_000_000
couponRate = 0.04

p = getBondPrice_Z(face, couponRate, times, yc)
print(f"Bond Price = ${p:,.2f}")
