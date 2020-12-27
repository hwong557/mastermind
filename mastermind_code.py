"""
This is the "code" class, which represents a code, number of right color right position pegs, and number of right color wrong position pegs.
There are functions to check if a given is compatible with another code, given number of correct position and wrong position pegs.
"""

import numpy as np
from typing import Iterable, Union, Sized, List
import itertools
from itertools import product

colors = {
        "blue": 0,
        "green": 1,
        "orange": 2,
        "purple": 3,
        "red": 4,
        "yellow": 5,
        "b": 0,
        "g": 1,
        "o": 2,
        "p": 3,
        "r": 4,
        "y": 5,
        "B": 0,
        "G": 1,
        "O": 2,
        "P": 3,
        "R": 4,
        "Y": 5,
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        }

class Code:
    def __init__(self,
            code: Union[str, List[str], List[int]],
            black: int = None,
            white: int = None,
            ) -> None:
        assert len(code)==4
        self.code: List[int]
        self.code = [ colors[color] for color in code ]
        # if isinstance(code, str):
        #     self.code = [ colors[color] for color in code ]
        # elif isinstance(code, List[str]):
        #     self.code = [ colors[color] for color in code ]
        # elif isinstance(code, List[int]):
        #     self.code = code
        self.num_correct = black
        self.num_permute = white

    def __repr__(self) -> str:
        num_to_color = {
                0: "B",
                1: "G",
                2: "O",
                3: "P",
                4: "R",
                5: "Y",
                }
        return f'{"".join([num_to_color[spot] for spot in self.code])} {self.num_correct} {self.num_permute}'

    def __eq__(self, other) -> bool:
        return self.code == other.code and self.num_correct == other.num_correct and self.num_permute == other.num_permute

    # other should be type "Code"
    def is_correct_compatible_with(self, other: 'Code') -> bool:
        num_correct = self.num_correct
        us = np.array(self.code)
        them = np.array(other.code)
        # print(self)
        return np.sum(us == them) == num_correct

    # other should be type "Code"
    def is_permute_compatible_with(self, other) -> bool:
        """
        """
        us = np.array(self.code)
        them = np.array(other.code)

        # Some janky code but it seems to work.
        comparison_matrix = np.zeros((4, 4), dtype=int)
        for i in range(4):
            comparison_matrix[i, i] = (us[i] == them[i])
        for row in range(4):
            for col in range(4):
                if (
                        us[row] == them[col] and
                        1 not in comparison_matrix[:, col] and
                        1 not in comparison_matrix[row, :]
                    ):
                    comparison_matrix[row, col] = 1
                    break
        # print(self)
        # print(comparison_matrix)
        for i in range(4):
            comparison_matrix[i, i] = 0
        return np.sum(comparison_matrix) == self.num_permute

    def is_compatible_with(self, other) -> bool:
        return self.is_correct_compatible_with(other) and self.is_permute_compatible_with(other)
