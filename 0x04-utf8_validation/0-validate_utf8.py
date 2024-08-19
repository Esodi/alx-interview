#!/usr/bin/python3
'''
 method that determines if a given data set represents a valid UTF-8 encoding.
'''

def validUTF8(data):
    ''' the function itself'''
    for i in data:
        j = i.to_bytes(4)
        try:
            j.decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False
