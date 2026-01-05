class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0

        elif n==1 or n==2:
            return 1

        else:
            num1 = 1
            num2 = 1
            for _ in range(3,n+1):
                res = num1 + num2
                num1 = num2
                num2 = res

            return res  

                
