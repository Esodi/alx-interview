#!/usr/bin/python3
'''
 method that determines if a given data set represents a valid UTF-8 encoding.
'''

def validUTF8(data):
    ''' the function itself'''
    num_byt = 0
    for i in data:
        if num_byt == 0:
            if i >> 5 == 0b110:
                num_byt = 1
            elif i >> 4 == 0b1110:
                num_byt = 2
            elif i >> 3 == 0b11110:
                num_byt = 3
            elif i >> 7 == 0:
                continue
        else:
            if i >> 6 != 0b10:
                return False
            num_byt -= 1
            
    return num_byt == 0
