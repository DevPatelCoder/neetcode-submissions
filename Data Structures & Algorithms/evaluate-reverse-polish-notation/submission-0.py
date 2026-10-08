class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                if len(stack)<2:
                    return False
                num2 = int(stack[-1])
                stack.pop()
                num1 = int(stack[-1])
                stack.pop()
                stack.append(num1+num2)
            elif token == "-":
                if len(stack)<2:
                    return False
                num2 = int(stack[-1])
                stack.pop()
                num1 = int(stack[-1])
                stack.pop()
                stack.append(num1-num2)
            elif token == "*":
                if len(stack)<2:
                    return False
                num2 = int(stack[-1])
                stack.pop()
                num1 = int(stack[-1])
                stack.pop()
                stack.append(num1*num2)
            elif token == "/":
                if len(stack)<2:
                    return False
                num2 = int(stack[-1])
                stack.pop()
                num1 = int(stack[-1])
                stack.pop()
                stack.append(int(num1/num2))
            else:
                stack.append(int(token))
        if len(stack) != 1:
            return False
        return stack[-1]