class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output = []
        # temp_list = []
        # for i in range(len(strs)):
        #     for j in range(i+1,len(strs)):
                
        #         if "".join(sorted(strs[i])) == "".join(sorted(strs[j])):
        #             temp_list.append(strs[j])
        #     temp_list.append(strs[i])
        # output.append(temp_list)
        # temp_list = []

        # return output

        output = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in output:
                output[key]=[]
            output[key].append(word)
        result = list(output.values())
        return result

            





        


        