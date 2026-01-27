class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        # if digits[0] != 9:
        #     digits[0]+=1
        #     return digits[::-1]

        # else:
        i=0
        while(i<len(digits)):
            if digits[i]==9:
                digits[i]=0
                i+=1
            else:
                digits[i]+=1
                return digits[::-1]

        digits.append(1)
        return digits[::-1]
            


            

        