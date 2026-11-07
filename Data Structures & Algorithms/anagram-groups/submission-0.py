class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            key = ''.join(sorted(word)) # sorted(word) creats a list like ['a','c',t'] but we want a word thus .join() joins them together with no space '' to get key = "act".
            if key not in d:
                d[key] = []
            d[key].append(word)
            
        return list(d.values())