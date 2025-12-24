class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}

        for number in nums:
            if number not in freq_map:
                freq_map[number] = 0
            freq_map[number] += 1

        sorted_freq = sorted(freq_map.items(), key = lambda p :p[1], reverse = True)
        return [pair[0] for pair in sorted_freq[:k]]
        