class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ", "").lower()
        string = ''.join(filter(str.isalnum, string))
        return string[::1] == string[::-1]
        