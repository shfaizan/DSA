class Solution:
    def isAnagram(self,s: str, t: str) -> bool:
        if sorted(t) ==sorted(s):
        # if sorted(list(t)) == sorted (list(s)):
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))
    print(s.isAnagram("a", "aa"))