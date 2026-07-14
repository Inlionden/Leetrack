class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            from collections import defaultdict
            gA=defaultdict(list)

            for wrd in strs:
                chr_list=[0]*26
                for ch in wrd:
                    chr_list[ord(ch)-ord('a')]+=1
                gA[tuple(chr_list)].append(wrd)
            
            return list(gA.values())