class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            #odd-length
            left = i
            right = i

            while left>=0 and right<len(s) and s[left]==s[right]:
                if right - left+1>len(longest):
                    longest = s[left:right+1]

                left-=1
                right +=1



            #Even-length

            left = i
            right = i+1
            while left>=0 and right <len(s) and s[right]==s[left]:
                if right - left+1>len(longest):
                    longest = s[left:right+1]

                left-=1
                right +=1

        return longest

        