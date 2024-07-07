#!/usr/bin/python3
''' lockboxes solver program '''


def canUnlockAll(boxes):
    ''' the function '''
    def recurse(n, open_boxes):
        ''' recursive function '''
        if n not in open_boxes:
            open_boxes.add(n)
            for i in boxes[n]:
                recurse(i, open_boxes)
        return open_boxes
    open_boxes = set()
    unlocked = recurse(0, open_boxes)
    return len(unlocked) == len(boxes)
