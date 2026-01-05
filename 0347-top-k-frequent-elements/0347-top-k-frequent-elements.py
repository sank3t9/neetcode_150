class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []
        res = []

        for num,freq in freq_map.items():
            heap.append((-freq,num))

        heapq.heapify(heap)
        print(heap)

        for _ in range(0,k):
            temp = heapq.heappop(heap)
            res.append(temp[1])

        return res
            


        