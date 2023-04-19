import argparse

from . import coder
from .predictions import pair_frequency
from .codepage import codepage


def vyxal_to_int(s):
    return [codepage.find(c) for c in s]

def int_to_vyxal(lst):
    return "".join(codepage[x] for x in lst)

pred = pair_frequency(2, 1/800)

def encode():
    parser = argparse.ArgumentParser(description='Encodes Vyxal code as a binary string.')
    parser.add_argument('code', type=str, help='Vyxal code to be encoded.')

    args = parser.parse_args()

    bin_lst = coder.encode(vyxal_to_int(args.code), pred)
    print("".join(str(b) for b in bin_lst))

def decode():
    parser = argparse.ArgumentParser(description='Decodes Vyxal code from a binary string.')
    parser.add_argument('str', type=str, help='String to be encoded.')

    args = parser.parse_args()

    int_lst = coder.decode([int(c) for c in args.str], pred)

    print(int_to_vyxal(int_lst))