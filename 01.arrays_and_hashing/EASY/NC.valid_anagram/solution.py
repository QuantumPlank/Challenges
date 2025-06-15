class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            characters[s[i]] = 1 + characters.get(s[i], 0)
            characters[t[i]] = -1 + characters.get(t[i], 0)
        
        for char in characters.keys():
            if characters[char] != 0:
                return False
        return True