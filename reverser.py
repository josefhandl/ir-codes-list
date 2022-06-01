#!/bin/python3

import sys

print(hex(int(bin(int(sys.argv[1], 16))[2:].zfill(16)[::-1], 2)).upper().replace('X', 'x'))
