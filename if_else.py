
import math
import os
import random
import re
import sys
   
if __name__ == '__main__':
    n = int(input().strip())
    assert (n >= 0 and n <= 100)
    if n % 2 != 0 or (n >= 6 and n <= 20 and n % 2 == 0):
        print("Weird")
    elif n % 2 == 0 and ((n >= 2 and n <= 5) or n > 20):
        print("Not Weird")
