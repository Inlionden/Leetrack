class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        s_l= len(s)
        win_c = 0
        max_s = 0
        vowel= "aeiou"

        win_c = sum(1 for c in s[:k] if c in vowel)
        max_s= max(max_s, win_c)
        for i in range(k, s_l):
            if s[i] in vowel:
                win_c+=1

            if s[i-k] in vowel:
                win_c-=1
            
            max_s= max(win_c, max_s)
        return max_s