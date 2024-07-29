#!/usr/bin/python3
''' the utf-8 verification module '''


def validUTF8(data):
    """function itself
    """
    if not all(0 <= x <= 255 for x in data):
        return False
    byt = bytes(data)
    try:
        byt.decode('utf-8')
        retrun True
    except UnicodeDecodeError:
        return False
