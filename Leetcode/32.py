class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
            return 0
        ans = [0] * len(s)
        if s[0] == '(' and s[1] == ')':
            ans[1] = 2
        else:
            ans[1] = 0
        for i in range(2, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    ans[i] = ans[i-2] + 2
                else:
                    if (i - ans[i-1] - 1)>-1 and s[i - ans[i-1] - 1] == '(':
                        ans[i] = ans[i-1] + ans[i - ans[i-1] -2] + 2
        # print(ans)
        return max(ans)