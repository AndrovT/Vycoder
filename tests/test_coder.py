import random
import csv
from vycoder.coder import *
from vycoder.predictions import frequency, pair_frequency

def test_bin_list():
    assert bin_list(7, 5) == [0, 0, 1, 1, 1]
    assert bin_list(37, 4) == [0, 1, 0, 1]


def test_coder1():
    pred = lambda x: [1, 1, 1, 1]

    lst = [0, 1, 2, 3]
    encoded = encode(lst, pred)
    assert encoded == [0, 0, 0, 1, 1, 0, 1, 1]
    assert decode(encoded, pred) == lst

def test_coder3():
    pred = lambda x: [1, 1, 1, 1]
    random.seed(0)
    lst = [random.randrange(4) for _ in range(100)]
    assert decode(encode(lst, pred), pred) == lst

def test_coder4():
    random.seed(0)
    distribution = [random.randrange(1, 20) for _ in range(100)]
    pred = lambda x: distribution

    lst = [random.randrange(100) for _ in range(1000)]
    assert decode(encode(lst, pred), pred) == lst

def test_coder5():
    with open("vycoder/TestData.csv", newline="") as f:
        for row in csv.reader(f):
            assert decode(encode([int(x) for x in row], frequency), frequency) == [int(x) for x in row]

def test_coder6():
    pred = pair_frequency(2, 1/800)
    with open("vycoder/TestData.csv", newline="") as f:
        for row in csv.reader(f):
            assert decode(encode([int(x) for x in row], pred), pred) == [int(x) for x in row]
