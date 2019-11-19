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
    _row: int
    _column: int

    def __init__(self, hashtable):
        self._hashtable = hashtable
        self._row = 0
        self._column = 0

    def __iter__(self):
        return self

    def _next(self):
        max_hashtable_row = self._hashtable._number_of_rows - 1
        if self._row > max_hashtable_row:
            raise StopIteration()

        records = self._hashtable._records
        result = records[self._row][self._column]

        self._column += 1
        max_hashtable_column = self._hashtable._number_of_columns - 1
        if self._column > max_hashtable_column:
            self._column = 0
            self._row += 1

        return result

    def __next__(self):
        next = self._next()
        while next is None:
            next = self._next()
        return next
        

class Hashtable(abc.Set):
    _records: List[List[HashtableRecord]]
    _number_of_rows: int
    _number_of_columns: int
    _hash_funcion: HashFunction = polynomialRollingHashFunction
    _len: int

    def __init__(self, rows=100, columns=10):
        self._records = [[None for __ in range(rows)] for __ in range(rows)]
        self._number_of_rows = rows
        self._number_of_columns = columns
        self._len = 0

    def add(self, string):
        hash = self._hash_funcion(string)
        new_hash_record = HashtableRecord(hash, string)
        row = hash % self._number_of_rows

        try:
            column_of_first_free_record = self._records[row].index(None)
            column = column_of_first_free_record
        except ValueError as exc:
            raise HashtableFullError() from exc

        self._records[row][column] = new_hash_record
        self._len += 1

    def indexes(self, string):
        hash = self._hash_funcion(string)
        searched_hash_record = HashtableRecord(hash, string)
        row = hash % self._number_of_rows

        try:
            column_of_searched_hash_record = self._records[row].index(searched_hash_record)
            column = column_of_searched_hash_record
        except ValueError as exc:
            raise HashtableEmptyError() from exc

        return row, column

    def discard(self, string):
        try:
            row, column = self.indexes(string)
        except HashtableEmptyError:
            return
        self._records[row][column] = None
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