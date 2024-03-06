#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:47:16 2024

@author: chenbailun
"""

import math

def calculate_circle(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area

def main():
    radius = float(input("請輸入圓的半徑："))
    circumference, area = calculate_circle(radius)
    print("圓周長為:", circumference)
    print("圓面積為:", area)

if __name__ == "__main__":
    main()
