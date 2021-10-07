from bplustree.Btree import Btree
from random import randint


def sample_upsert(bt, n, minimum, maximum):
    for i in range(n):
        key = randint(minimum, maximum)
        value = randint(minimum, maximum)
        bt.upsert(key, value)


def sample_predecessor(bt, times, minimum, maximum):
    for i in range(times):
        key = randint(minimum, maximum)
        print("predecessor: key", key, ", ans", bt.predecessor(key))
    print()


def sample_successor(bt, times, minimum, maximum):
    for i in range(times):
        key = randint(minimum, maximum)
        print("successor: key", key, ", ans", bt.successor(key))
    print()


def sample_range(bt, times, minimum, maximum, range_size):
    for i in range(times):
        key = randint(minimum, maximum)
        first = max(minimum, key - range_size // 2)
        end = min(maximum, key + range_size // 2)
        ans = bt.range(first, end)
        print("range [", first, ",", end, "]:")
        print(" ", ans)


def main():
    N = 1000
    TIMES = 10
    MINIMUM = 0
    MAXIMUM = 10000
    bt = Btree()

    sample_upsert(bt, N, MINIMUM, MAXIMUM)

    bt.print()
    print()

    sample_predecessor(bt, TIMES, MINIMUM, MAXIMUM)
    sample_successor(bt, TIMES, MINIMUM, MAXIMUM)
    sample_range(bt, TIMES, MINIMUM, MAXIMUM, (MAXIMUM - MINIMUM) // 100)

    return


if __name__ == "__main__":
    main()
