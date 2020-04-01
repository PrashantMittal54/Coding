# Insertion Sort

import numpy as np

array = list(np.random.permutation(10))     # generating random numbers


def insertion_sort(arr):
    for j in range(1, len(arr)):
        sortdAry = arr[:j]
        key = arr[j]
        flip = False
        for i in range(len(sortdAry)):
            if not flip:
                if sortdAry[i] > key:
                    key, sortdAry[i] = sortdAry[i], key
                    flip = True
            else:
                key, sortdAry[i] = sortdAry[i], key
        arr = sortdAry + [key] + arr[j+1:]
    return arr


output = insertion_sort(array)
print(output)