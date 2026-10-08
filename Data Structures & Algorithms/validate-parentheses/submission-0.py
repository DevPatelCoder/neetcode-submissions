class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack[-1]

                if char ==')'and top!='(':
                    return False
                if char =='}'and top!='{':
                    return False
                if char ==']'and top!='[':
                    return False

                stack.pop()
        return len(stack)==0