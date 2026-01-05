class Solution:
    def fib(self, n: int) -> int:
        # def recursion(num):
        #     if num==0:
        #         return 0
        #     if num==1:
        #         return 1

        #     return recursion(num-1)+recursion(num-2)

        # return recursion(n)
        if n==0:
            return 0

        elif n==1 or n==2:
            return 1

        else:
            num1 = 1
            num2 = 1
            for i in range(3,n+1):
                res = num1 + num2
                num1 = num2
                num2 = res

            return res  
                
