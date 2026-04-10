class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        list_dict = []

        for e in strs:
            dict_e = {}
            for lettre in e:
                if lettre in dict_e:
                    dict_e[lettre] += 1
                else:
                    dict_e[lettre] = 1
            list_dict.append((e, dict_e)) 

        temp_list_dict = list_dict.copy()

        while temp_list_dict:
            mot, dict_ref = temp_list_dict.pop(0)
            temp_list = [mot]
            

            j = 0
            while j < len(temp_list_dict):
                if dict_ref == temp_list_dict[j][1]:
                    temp_list.append(temp_list_dict.pop(j)[0])
                else:
                    j += 1

            result.append(temp_list)
        return result