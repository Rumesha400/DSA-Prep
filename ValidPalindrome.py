class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = "".join(ch.lower() for ch in s if ch.isalnum())
        return original == original[::-1]
