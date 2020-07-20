import numpy as np
import random

part_id = []

# for i in range(9):
#     part_id.append(i)
"""
define part id:

top-left = 0        -           top-right = 1
    \                              /
        left-eye = 2    -    right-eye = 3
                \               /
|                   nose = 4                |
            /                   \
        mouth-left = 5  - mouth-right = 6
        /                           \
buttom-left = 7       -         buttom-right = 8


define graph:

using a list to store the graph, each element indicates to one node.
The element store a sub-list, storing the nodes link to the the current node (see the links above)
As we can see, each node links to three neighbours, except the mouth, which has four.

The order of linked node is following the clockwise. (from left to right)
"""

# build the graph
part_id.append(1, 2, 7)

part_id.append(0, 3, 8)

part_id.append(0, 3, 4)

part_id.append(2, 1, 4)

part_id.append(2, 3, 5, 6)

part_id.append(4, 6, 7)

part_id.append(5, 4, 8)

part_id.append(0, 5, 7)

part_id.append(7, 6, 1)


# define naive random function
# part_id: the graph
# the number of iteration will preform
def random_walk(part_id, itre_num = 2):
    path = []
    # random pick a start point
    current_point = random.randrange(9)
    path.append(current_point)
    for i in range(itre_num):
        path.append(random.choice(part_id[current_point]))

    return path


# modify the landmarks based on the result of random
def landmark_random_walk(landmarks, path):
    modified_landmarks = []

    for landmark in landmarks:
        temp_list = []
        
        for node in path:
            temp_list.append(landmark[node])

        modified_landmarks.append(temp_list)

    return modified_landmarks