"""Tests for hashtableanalysis.hashtable.hashtable"""

from hashtableanalysis.hashtable.hashtable import Hashtable


def test_hashtable_add():
    hashtable = Hashtable()
    string = 'AbCdEfG'

    assert string not in hashtable 
    hashtable.add(string)
    assert string in hashtable
