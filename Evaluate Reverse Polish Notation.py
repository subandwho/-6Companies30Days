def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators= ['+', '-', '*', '/']
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                if len(stack) >= 2:
                    if i == '+':
                        stack[-2] = stack[-2] + stack[-1]
                        stack.pop()
                    elif i == '-':
                        stack[-2] = stack[-2] - stack[-1]
                        stack.pop()
                    elif i == '*':
                        stack[-2] = stack[-2] * stack[-1]
                        stack.pop()
                    elif i == '/':
                        stack[-2] = int(stack[-2] / stack[-1])
                        stack.pop()
        return stack[0]
