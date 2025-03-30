# w.o. ps[i-1]
# 스택에 수 넣기
def solution(PS):
    stack = []
    result = 0

    for ps in PS:

        if ps in ('(', '['):
            stack.append(ps)

        elif ps == ')':

            temp = 0
            while stack and isinstance(stack[-1], int):
                temp += stack.pop()

            if stack and stack[-1] == '(':
                stack.pop()
                stack.append(2 * temp if temp else 2)

            else:
                return 0


        else: # ps == ']'

            temp = 0
            while stack and isinstance(stack[-1], int):
                temp += stack.pop()

            if stack and stack[-1] == '[':
                stack.pop()
                stack.append(3 * temp if temp else 3)

            else:
                return 0

    while stack:

        top = stack.pop()
        if isinstance(top, int):
            result += top
        else:
            return 0

    return 0 if stack else result

# input
PS = input()

# solution
print(solution(PS))