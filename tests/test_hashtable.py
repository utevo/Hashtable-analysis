"""Tests for hashtableanalysis.hashtable.hashtable"""

from hashtableanalysis.hashtable.hashtable import Hashtable


def test_hashtable_add():
    hashtable = Hashtable()
    string = 'AbCdEfG'

    assert string not in hashtable 
    hashtable.add(string)
    assert string in hashtable


def test_hashtable_discard():
    hashtable = Hashtable()
    string = 'AbCdEfG'

    assert string not in hashtable 
    hashtable.discard(string)
    assert string not in hashtable

    hashtable.add(string)
    assert string in hashtable
    hashtable.discard(string)
    assert string not in hashtable
    hashtable.discard(string)
    assert string not in hashtable
