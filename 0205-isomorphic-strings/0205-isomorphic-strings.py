class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_t={}
        t_s={}

        for cs, ct in zip(t,s):
            if cs in s_t:
                if s_t[cs]!=ct:
                    return False
            else:
                s_t[cs]=ct

            if ct in t_s:
                if t_s[ct]!=cs:
                    return False
            else:
                t_s[ct]=cs
        return True

        

