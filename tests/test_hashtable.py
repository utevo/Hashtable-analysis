"""Tests for hashtableanalysis.hashtable.hashtable"""

from hashtableanalysis.hashtable.hashtable import Hashtable


def test_hashtable_add():
    hashtable = Hashtable()
    string = 'Ambroży'

    assert string not in hashtable 
    hashtable.add(string)
    assert string in hashtable


def test_hashtable_discard():
    hashtable = Hashtable()
    string = 'Ambroży'

    assert string not in hashtable 
    hashtable.discard(string)
    assert string not in hashtable

    hashtable.add(string)
    assert string in hashtable
    hashtable.discard(string)
    assert string not in hashtable
    hashtable.discard(string)
    assert string not in hashtable


def test_hashtable_len():
    hashtable = Hashtable()
    string_1 = 'Ambroży'
    string_2 = 'Kleks'

    assert len(hashtable) == 0
    hashtable.add(string_1)
    assert len(hashtable) == 1
    hashtable.add(string_2)
    assert len(hashtable) == 2

    hashtable.discard(string_1)
    assert len(hashtable) == 1
    hashtable.discard(string_1)
    assert len(hashtable) == 1

    hashtable.discard(string_2)
    assert len(hashtable) == 0
    hashtable.discard(string_2)
    assert len(hashtable) == 0


def test_hashtableiterator_init():
    hashtable = Hashtable()

    iterator = iter(hashtable)
    assert iterator == iter(iterator)


def test_hashtableiterator_next():
    hashtable = Hashtable()
    string_1 = 'Ambroży'
    string_2 = 'Kleks'
    string_3 = 'Mucholot'
    hashtable.add(string_1)
    hashtable.add(string_2)
    hashtable.add(string_3)

    iterator = iter(hashtable)
    strings = set()
    try:
        while True:
            string = next(iterator)
            strings.add(string)
    except StopIteration:
        pass

    assert strings == {string_1, string_2, string_3}

def test_hashtableiterator_iteratrion_by_for():
    hashtable = Hashtable()
    string_1 = 'Ambroży'
    string_2 = 'Kleks'
    string_3 = 'Mucholot'
    hashtable.add(string_1)
    hashtable.add(string_2)
    hashtable.add(string_3)

    strings = set()
    for string in hashtable:
        strings.add(string)

    assert strings == {string_1, string_2, string_3}