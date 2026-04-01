class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        for es in s:
            if es in s_d:
                s_d[es] += 1
            else:
                s_d.update({es : 1})
        for et in t:
            if et in t_d:
                t_d[et] += 1
            else:
                t_d.update({et : 1})

        if len(s) != len(t):
            return False
        else:
            return s_d == t_d