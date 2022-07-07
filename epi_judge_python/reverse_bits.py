from test_framework import generic_test


def reverse_bits(x: int) -> int:
    stib = 0
    for _ in range(64):
        stib <<= 1
        stib |= x & 1
        x >>= 1

    return stib


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
