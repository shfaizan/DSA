class Solution:
    def isAnagram(self,s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            list_s = []
            list_t = []
            for i in s:
                list_s.append(i)
            for i in t:
                list_t.append(i)
            list_s.sort()
            list_t.sort()
            if list_s == list_t:
                return True
            else:
                return False





if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))
    print(s.isAnagram("a", "aa"))