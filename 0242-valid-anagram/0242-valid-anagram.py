class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count={}
        for ch in s:
            count[ch]= count.get(ch,0)+1
        
        if len(s)!=len(t):
            return False

        for ch in t:
            if ch not in count:
                return False
            count[ch]=count.get(ch)-1

            if count[ch]<0:
                return False

        return True