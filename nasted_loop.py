#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a Nested Loops program.


def main():
    # This is the function to run Nested Loops.

    counter1 = 0
    counter2 = 0
    counter3 = 0

    # Process & output
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("RGB({0},{1},{2})".format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
