from collections import namedtuple
from typing import Callable, List

from hashtableanalysis.hashtable.hashfunctions import (
    HashFunction, polynomialRollingHashFunction)


class HashtableRecord:
    hash: int
    value: str

    def __init__(self, hash: int, value: str):
        self.hash = hash
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, HashtableRecord):
            return False

        is_hash_eq = self.hash == other.hash
        is_value_eq = self.value == other.value
        return is_hash_eq and is_value_eq

    def __repr__(self):
        return repr({'hash': self.hash, 'value': self.value})


class HashtableFullError(Exception):
    pass


class HashtableEmptyError(Exception):
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

    def add(self, string):
        hash = self._hash_funcion(string)
        new_hash_record = HashtableRecord(hash, string)
        index_x = hash % self._lenght

        try:
            index_y_of_first_free_record = self._records[index_x].index(None)
            index_y = index_y_of_first_free_record
        except ValueError as exc:
            raise HashtableFullError() from exc
        
        self._records[index_x][index_y] = new_hash_record
           
    def discard(self, string):
        hash = self._hash_funcion(string)
        searched_hash_record = HashtableRecord(hash, string)
        index_x = hash % self._lenght

        try:
            index_y_of_searched_hash_record = self._records[index_x].index(searched_hash_record)
            index_y = index_y_of_searched_hash_record
        except ValueError as exc:
            raise HashtableEmptyError() from exc

        self._records[index_x][index_y] = None

    def __contains__(self, string):
        hash = self._hash_funcion(string)
        searched_hash_record = HashtableRecord(hash, string)
        index_x = hash % self._lenght

        try:
            index_y_of_searched_hash_record = self._records[index_x].index(searched_hash_record)
            index_y = index_y_of_searched_hash_record
        except ValueError:
            return False
        return True

    def __repr__(self):
        return repr(self._records)


if __name__ == '__main__':
    hashtable = Hashtable()
