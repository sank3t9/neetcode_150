import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)

        #early exit
        max_freq = 0
        for char in freq_map:
            if freq_map[char] > max_freq:
                max_freq = freq_map[char]

        if max_freq > (len(s) + 1) // 2:
            return ""

        max_heap = []
        for char,count in freq_map.items():
            max_heap.append((-count,char))

        heapq.heapify(max_heap)
        

        prev_count, prev_char = 0, ""
        res = []

        while(max_heap):
            count, char = heapq.heappop(max_heap)
            count = (-1)*count
            res.append(char)

            count -= 1

            if prev_count > 0:
                heapq.heappush(max_heap, (-prev_count, prev_char))

            prev_count, prev_char = count, char

        if len(res) == len(s):
            return "".join(res)

        else:
            return "" 