"""
Alternative pin mappings for Orange PI PC(see
https://linux-sunxi.org/Xunlong_Orange_Pi_PC)

Usage:

.. code:: python
   import orangepi.4
   from OPi import GPIO

   GPIO.setmode(orangepi.4.BOARD)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be 3 * 32 +14 = 110

BOARD = {
    3:   64,  
    5:   65,    
    7:  150, 
    8:  145,
    10: 144, 
    11:  33,
    12:  50,
    13:  35,
    15:  92, 
    16:  54, 
    18:  55,
    19:  40,
    21:  39,
    22:  56,
    23:  41,
    24:  42,  
    26: 149, 
    27:  64,
    28:  65,
    29:  -1,
    31:  -1,
    32:  -1,
    33:  -1,
    35:  -1,
    36:  -1,
    37:  -1,
    38:  -1,
    40:  -1,
}


# Orangepi 4 BCM pin to actual GPIO pin
BCM = BOARD
