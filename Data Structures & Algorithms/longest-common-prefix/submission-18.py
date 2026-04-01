class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            lettre = strs[0][i]
            for element in strs:
                statement = True
                if i >= len(element) or element[i] != lettre:
                    return result
            if statement:
                result += lettre
            else:
                break
        return result