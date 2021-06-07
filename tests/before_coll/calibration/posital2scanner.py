#!/usr/bin/python
# coding: utf-8
import sys
import numpy as np

def main():

# Posital      Laserscanner
# 802871       -5.0177  
# 690575        0.0192
# 578079        4.9862  
# 465680         9.9888
# 353283        14.9897
# 241035        19.9951
# 128723        24.9998
# 16436         29.9965
# -95945        35.0005
# -208445       40.0095
# -320921       45.01
# 

  enc = np.array([802871,
                  690575,
                  578079,
                  465680,
                  353283,
                  241035,
                  128723,
                  16436,
                  -95945,
                  -208445,
                  -320921])

  ref = np.array([-5.0177,
                  0.0192,
                  4.9862, 
                  9.9888,
                  14.9897,
                  19.9951,
                  24.9998,
                  29.9965,
                  35.0005,
                  40.0095,
                  45.01])
                  
  z = np.polyfit(enc, ref, 1)

  print(z)
  
if __name__ == "__main__":
  main()
