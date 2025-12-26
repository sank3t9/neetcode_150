class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # FIrst thing that came to my mind
        # answer = ""
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         answer += s[i].lower()
        
        # reverse_answer = answer[::-1]

        # return answer == reverse_answer

        #trying using two pointers
        left, right = 0, len(s)-1

        while(left<=right):
            if not s[left].isalnum():
                left +=1
                continue

            if not s[right].isalnum():
                right -=1
                continue
          
            if(s[left].lower()==s[right].lower()):
                left+=1
                right-=1
            else:
                return False

        return True



                