"""Tests for hashtableanalysis.hashtable."""

from hashtableanalysis.hashtable import hashtable, hashfunction 


def test_polynomial_rolling_hash_function():
    hash_function = hashfunction.PolynomialRollingHashFunction()

    input = '123'
    output = hash_function(input)
    assert output == 12341