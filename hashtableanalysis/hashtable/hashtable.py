from collections import namedtuple
from typing import List, Callable

from hashtableanalysis.hashtable.hashfunction import HashFunction, PolynomialRollingHashFunction


class HashtableRecord:
    hash: int
    value: str


class Hashtable:
    _records: List[List[HashtableRecord]]
    _hash_funcion: HashFunction = PolynomialRollingHashFunction()

    def __init__(self, lenght=100, width=10):
        self._records = [[HashtableRecord() for __ in range(width)] for __ in range(lenght)]


if __name__ == '__main__':
    hashtable = Hashtable()
