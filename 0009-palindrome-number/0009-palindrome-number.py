class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        to_string = str(abs(x))
        reverse = to_string[::-1]
        to_int = int(reverse)

        return to_int == x
        