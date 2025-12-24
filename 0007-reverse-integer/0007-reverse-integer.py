class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign = -1
        else :
            sign = 1

        to_string = str(abs(x))
        reverse = to_string[::-1]
        to_int = int(reverse) * sign

        if (to_int < -2**31 or to_int > 2**31 - 1) :
            return 0
        else:
            return to_int
        