from collections import namedtuple
from collections import abc
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
        return f"HashtableRecord(hash='{self.hash}', value='{self.value}')"


class HashtableFullError(Exception):
    pass


class HashtableEmptyError(Exception):
    pass


class HashtableIterator(abc.Iterator):
    _hashtable: object
    _index_x: int
    _index_y: int

    def __init__(self, hashtable):
        self._hashtable = hashtable
        self._index_x = 0
        self._index_y = 0

    def __iter__(self):
        return self

    def _next(self):
        hashtable_max_index_x = self._hashtable._lenght - 1
        if self._index_x > hashtable_max_index_x:
            raise StopIteration()

        result = self._hashtable._records[self._index_x][self._index_y]

        self._index_y += 1
        hashtable_max_index_y = self._hashtable._width - 1
        if self._index_y > hashtable_max_index_y:
            self._index_y = 0
            self._index_x += 1

        return result

    def __next__(self):
        next = self._next()
        while next is None:
            next = self._next()
        return next
        

class Hashtable(abc.Set):
    _records: List[List[HashtableRecord]]
    _lenght: int
    _width: int
    _hash_funcion: HashFunction = polynomialRollingHashFunction
    _len: int

    def __init__(self, lenght=100, width=10):
        self._records = [[None for __ in range(width)] for __ in range(lenght)]
        self._lenght = lenght
        self._width = width
        self._len = 0

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
        self._len += 1

    def indexes(self, string):
        hash = self._hash_funcion(string)
        searched_hash_record = HashtableRecord(hash, string)
        index_x = hash % self._lenght

        try:
            index_y_of_searched_hash_record = self._records[index_x].index(searched_hash_record)
            index_y = index_y_of_searched_hash_record
        except ValueError as exc:
            raise HashtableEmptyError() from exc

        return index_x, index_y

    def discard(self, string):
        try:
            index_x, index_y = self.indexes(string)
        except HashtableEmptyError:
            return
        self._records[index_x][index_y] = None
        self._len -= 1

    def __contains__(self, string):
        try:
            self.indexes(string)
        except HashtableEmptyError:
            return False
        return True

    def __len__(self):
        return self._len

    def __iter__(self):
        return HashtableIterator(self)

    def __repr__(self):
        return repr(self._records)