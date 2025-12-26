class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            odd_pal = self.expand(s,i,i)
            
            even_pal = self.expand(s,i,i+1)
            best_at_i = max(odd_pal, even_pal, key=len)

            if len(best_at_i) > len(answer):
                answer = best_at_i

        return answer




    def expand(self, s: str, left: int, right: int) -> str:
        while(left>=0 and right<len(s) and s[left]==s[right]):

            left  -= 1
            right += 1

        return s[left+1:right]

        