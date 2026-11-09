class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s))+"#"+s     # I made a mistake here by not putting += 
        return string

    def decode(self, s: str) -> List[str]:
        res,i = [],0
        while i < len(s):
            j = i
            while s[j]!= "#":             # I made a mistake here by forgetting str[j]
                j+=1
            length = int(s[i:j])      # I forgot we had to calculate the length 
            res.append(s[j+1:j+1+length]) # I forgot the str[] in here
            i = j+1+length         # I also forgot to increment the i here and made a mistake by using += instead of =
        return res
