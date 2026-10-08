class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] =='0':
            return 0

        dp1 = 1
        dp2 = 1
        for i in range(1,len(s)):
            if int(s[i]) == 0 and int(s[i-1]) not in (1,2):
                return 0
            if int(s[i-1])!=0 and int(s[i-1:i+1])<=26:
                temp = dp1
                if int(s[i]) !=0:
                    temp +=dp2
            else:
                temp = dp2
            dp1 =dp2
            dp2 =temp
        return dp2