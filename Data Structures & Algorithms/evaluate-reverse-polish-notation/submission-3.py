class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calculate = []
        operators = {'+','-','/','*'}
        for i, c in enumerate(tokens):
            if c in operators:
                right = int(calculate.pop())
                left = int(calculate.pop())
                if(c == '+'):
                    result = left + right
                elif(c == '-'):
                    result = left-right
                elif(c=='/'):
                    result = int(left/right)    # add a int so it doesn't return float
                else:
                    result = left*right
                calculate.append(result)
            else:
                calculate.append(int(c))

        return calculate[0]



