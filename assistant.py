"""
This contains code to winnow down to the secret code.
"""

from mastermind_code import Code
import itertools
from typing import List, Iterator, Generator

attempts: List[Code] = []

all_codes: List[Code] = [ Code(list(code)) for code in itertools.product(range(6), repeat=4) ]

def all_possible_codes(all_codes: List[Code], attempts: List[Code]) -> Generator:
    for candidate in all_codes:
        if all([attempt.is_compatible_with(candidate) for attempt in attempts]):
            yield candidate
