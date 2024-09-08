#!/usr/bin/env python3
# Fibonacci Sequence
# The Fibonacci Sequence is the series of numbers:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# The next number is found by adding up the two numbers before it:

# the 2 is found by adding the two numbers before it (1+1),
# the 3 is found by adding the two numbers before it (1+2),
# the 5 is (2+3),
# and so on!
# Example: the next number in the sequence above is 21+34 = 55
# It is that simple!

# Here is a longer list:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144,233,377,610,987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, ...


def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
        print(fibonacci_sequence)
    