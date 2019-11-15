from collections import namedtuple
from typing import List, Callable

from hashtableanalysis.hashtable.hashfunctions import HashFunction, polynomialRollingHashFunction


class HashtableRecord:
    hash: int
    value: str

    def __init__(self, hash: int, value: str):
        self.hash = hash
        self.value = value

    def __repr__(self):
        return {'hash': self.hash, 'value': self.value}


class HashtableFullError(Exception):
    pass


class Hashtable:
    _records: List[List[HashtableRecord]]
    _lenght: int
    _width: int
    _hash_funcion: HashFunction = polynomialRollingHashFunction


    def __init__(self, lenght=100, width=10):
        self._records = [[None for __ in range(width)] for __ in range(lenght)]
        self._lenght = lenght
        self._width = width

    def add(self, word):
        hash = self._hash_funcion(word)
        new_hash_record = HashtableRecord(hash, word)

        index_x = hash % self._lenght

        try:
            index_of_first_free_record = self._records[index_x].index(None)
            self._records[index_x][index_of_first_free_record] = new_hash_record
        except ValueError as exc:
            raise HashtableFullError() from exc

    def __repr__(self):
        return repr(self._records)


if __name__ == '__main__':
    hashtable = Hashtable()
