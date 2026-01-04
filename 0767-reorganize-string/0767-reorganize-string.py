import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)
        max_heap = []
        for char,count in freq_map.items():
            max_heap.append((-count,char))

        heapq.heapify(max_heap)
        

        prev = None
        res = []

        while(max_heap):
            count, char = heapq.heappop(max_heap)
            res.append(char)

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if count + 1 < 0:
                prev = (count +1, char)

        if len(res) == len(s):
            return "".join(res)

        else:
            return "" 