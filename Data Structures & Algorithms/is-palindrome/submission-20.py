class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(' ', '')
        new = ''.join(filter(str.isalnum, s)).lower()
        i, j = 0, len(new) - 1
        print(new)
        while i < j:
            if new[i] == new[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
        