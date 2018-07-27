class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        b = s[::-1]
        if s == b:
            return True
        else:
            return False
