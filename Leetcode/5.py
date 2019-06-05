class Solution(object):
    def isp(self, s):
        a, b = 0, len(s) - 1
        while a < b:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return s
        ans = [1] * len(s)
        for i in range(1, len(s)):
            if ans[i - 1] == 1 and s[i] == s[i - 1]:
                ans[i] = 2
            if i - ans[i - 1] - 1 > -1 and s[i] == s[i - ans[i - 1] - 1]:
                ans[i] = ans[i - 1] + 2
            elif ans[i - 1] > 1:
                for j in range(i - ans[i - 1], i):
                    if self.isp(s[j:i + 1]):
                        ans[i] = i - j + 1
                        break

            if s[i] == s[i - 1] and ans[i - 1] - ans[i - 2] == 1 and i - 2 > -1:
                ans[i] = ans[i - 1] + 1
        m = max(ans)
        p = ans.index(m)
        return s[p - m + 1:p + 1]