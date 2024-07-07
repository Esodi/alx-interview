#!/usr/bin/python3
''' lockboxes solver program '''


def canUnlockAll(boxes):
    ''' the function '''
    def recurse(n, open_boxes):
        ''' recursive function '''
        if n in open_boxes:
            return
        open_boxes.add(n)
        for i in boxes[n]:
            if i < len(boxes):
                recurse(i, open_boxes)
    open_boxes = set()
    recurse(0, open_boxes)
    return len(open_boxes) == len(boxes)
