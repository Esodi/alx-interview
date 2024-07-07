#!/usr/bin/python3
''' lockboxes solver program '''


from collections import deque


def canUnlockAll(boxes):
    ''' the function '''
    open_boxes = set()
    queue = deque([0])

    while queue:
        box = queue.popleft()
        if box not in open_boxes:
            open_boxes.add(box)
            for key in boxes[box]:
                if key < len(boxes) and key not in open_boxes:
                    queue.append(key)
    return len(open_boxes) == len(boxes)
