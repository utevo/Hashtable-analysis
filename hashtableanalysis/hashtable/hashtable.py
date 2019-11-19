from __future__ import annotations

from collections import namedtuple
from collections import abc
from typing import Callable, List, Union, Tuple

from hashtableanalysis.hashtable.hashfunctions import (
    HashFunction, polynomialRollingHashFunction)


class HashtableRecord:
    hash: int
    value: str

    def __init__(self, hash: int, value: str):
        self.hash = hash
        self.value = value

    def __eq__(self, other: HashtableRecord) -> bool:
        if not isinstance(other, HashtableRecord):
            return False

        is_hash_eq = self.hash == other.hash
        is_value_eq = self.value == other.value
        return is_hash_eq and is_value_eq

    def __repr__(self) -> str:
        return f"HashtableRecord(hash='{self.hash}', value='{self.value}')"


class HashtableRowFullError(Exception):
    pass


class HashtableRowEmptyError(Exception):
    pass


class HashtableIterator(abc.Iterator):
    _hashtable: object
    _row: int
    _column: int

    def __init__(self, hashtable):
        self._hashtable = hashtable
        self._row = 0
        self._column = 0

    def __iter__(self) -> HashtableIterator:
        return self

    def _next_cell(self) -> Union[HashtableRecord, None]:
        max_hashtable_row = self._hashtable._number_of_rows - 1
        if self._row > max_hashtable_row:
            raise StopIteration()

        cells = self._hashtable._cells
        result = cells[self._row][self._column]

        self._column += 1
        max_hashtable_column = self._hashtable._number_of_columns - 1
        if self._column > max_hashtable_column:
            self._column = 0
            self._row += 1

        return result

    def _next_record(self) -> HashtableRecord:
        next = self._next_cell()
        while next is None:
            next = self._next_cell()
        return next

    def __next__(self) -> str:
        record = self._next_record()
        return record.value


class Hashtable(abc.Set):
    _cells: List[List[Union[HashtableRecord, None]]]
    _number_of_rows: int
    _number_of_columns: int
    _hash_funcion: HashFunction = polynomialRollingHashFunction
    _len: int

    def __init__(self, rows=100, columns=10):
        self._cells = [[None for __ in range(rows)] for __ in range(rows)]
        self._number_of_rows = rows
        self._number_of_columns = columns
        self._len = 0

    def add(self, string: str) -> None:
        hash = self._hash_funcion(string)
        new_hash_record = HashtableRecord(hash, string)
        row = hash % self._number_of_rows

        try:
            column_of_first_free_record = self._cells[row].index(None)
            column = column_of_first_free_record
        except ValueError as exc:
            raise HashtableRowFullError() from exc

        self._cells[row][column] = new_hash_record
        self._len += 1

    def _indexes(self, string: str) -> Tuple[int, int]:
        hash = self._hash_funcion(string)
        searched_hash_record = HashtableRecord(hash, string)
        row = hash % self._number_of_rows

        try:
            column_of_searched_hash_record = self._cells[row].index(searched_hash_record)
            column = column_of_searched_hash_record
        except ValueError as exc:
            raise HashtableRowEmptyError() from exc

        return row, column

    def discard(self, string: str) -> None:
        try:
            row, column = self._indexes(string)
        except HashtableRowEmptyError:
            return
        self._cells[row][column] = None
        self._len -= 1

    def __contains__(self, string: str) -> bool:
        try:
            self._indexes(string)
        except HashtableRowEmptyError:
            return False
        return True

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> HashtableIterator:
        return HashtableIterator(self)

    def __repr__(self) -> str:
        return repr(self._cells)
