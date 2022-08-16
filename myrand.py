#!/bin/env python3
import random


def myrand(n):
    num = []
    num.append(random.randint(1, 9))
    for _ in range(n-1):
        num.append(random.randint(1, 9))
    return num


def main():
    length = input('enter the length of number ')

    rnum = myrand(int(length))
    rnum_str = ''.join(str(i) for i in rnum)
    print(rnum_str)


if __name__ == "__main__":
    main()
