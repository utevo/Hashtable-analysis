from typing import List
from random import randrange

def wordgenerator(words: List[str]):
    while True:
        rand_number = randrange(len(words))
        yield words[rand_number]
