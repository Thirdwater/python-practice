"""A solution to leetcode problem 1342
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""
import math


class Solution:
    def numberOfSteps(self, num: int) -> int:
        # naive solution from just following the steps
        num_steps = 0
        while num != 0:
            if self.isPowerOfTwo(num):
                # Small shortcut for powers of 2.
                # We can keep dividing by 2 down to 1,
                # followed by another operation to get to 0.
                num_steps += int(math.log(num, 2)) + 1
                break
            else:
                if num % 2 == 0:
                    num //= 2
                else:
                    num -= 1
                num_steps += 1
        return num_steps

    def isPowerOfTwo(self, num: int) -> bool:
        # See https://stackoverflow.com/a/600306
        #
        # For powers of 2, the binary representation and the integer before it are:
        #   100...000
        #   011...111
        # and bitwise-and would produce 000...000 = 0
        #
        # For non-powers of 2:
        #   If it's odd, then num and num-1 only differ by the right-most bit
        #   and their &-sum will still have at least a 1 bit in the left-most position.
        #     n:          1xxxx1
        #     n-1:        1xxxx0
        #                 ------
        #     n & (n-1):  1xxxx0
        #
        #   Note that 1 is a special case since it's odd but 2^0 = 1.
        #   In this case, 1 & 0 = 0 so we are fine. All other odd numbers will
        #   have at least 2 bits.
        #
        #   If it's even, since it's not a power of 2,
        #   there will be at least a 1 bit in a non-left-most and non-right-most position.
        #   Now their &-sum will differ up to this 1 bit,
        #   so it will also have at least a 1 bit in the left-most position.
        #     n:          1xxxx100..00
        #     n-1:        1xxxx011..11
        #                 ------------
        #     n & (n-1):  1xxxx000..00
        return (num & (num - 1)) == 0 and num != 0
