class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        memo_a ={}
        memo_b = {}

        def countA(n):
            if n in memo_a:
                return memo_a[n]

            if n==1:
                return 6

            memo_a[n] = (3 * countA(n - 1) + 2 * countB(n - 1)) % MOD
            return memo_a[n]

        def countB(n):
            if n in memo_b:
                return memo_b[n]

            if n==1:
                return 6

            memo_b[n] = (2 * countA(n - 1) + 2 * countB(n - 1)) % MOD
            return memo_b[n]


        return (countA(n) + countB(n)) % MOD