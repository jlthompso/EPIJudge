from test_framework import generic_test


def swap_bits(x, i, j):
    a = (x >> i) & 1
    b = (x >> j) & 1
    if a != b:
        if a:
            x ^= 2 ** i
            x |= 2 ** j
        else:
            x |= 2 ** i
            x ^= 2 ** j

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
