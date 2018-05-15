#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""solution."""

import math
import sys

import numpy as np


def spiral_matrix(matrix) -> str:
    out = []
    while (matrix.size):
        out.append(matrix[0])
        matrix = matrix[1:].T[::-1]
    return ''.join(np.concatenate(out))


def transform_string(input_string: str) -> str:
    matrix_size = math.sqrt(len(input_string))
    matrix = np.array(list(input_string)).reshape((int(matrix_size),
                                                   int(matrix_size)))

    matrix = np.rot90(np.rot90(matrix))
    return spiral_matrix(matrix)


if __name__ == '__main__':   
    print(transform_string(sys.argv[1]), end='')
