# https://www.acmicpc.net/problem/2504
# VPS + 괄호 값 계산

def solution(ps):

    total = 0 # 최종 반환 값
    val = 1 # 괄호가 완성된 후 total에 더해줄 값
    stack = []

    for i in range(len(ps)):

        if ps[i] == '(':
            stack.append('(')
            val *= 2

        elif ps[i] == '[':
            stack.append('[')
            val *= 3

        elif ps[i] == ')':

            if stack and stack[-1] == '(':
                stack.pop()

                if ps[i-1] == '(' :
                    total += val

                val //= 2

            else : # empty stack or [...)
                return 0

        elif ps[i] == ']':

            if stack and stack[-1] == '[':
                stack.pop()

                if ps[i-1] == '[':
                    total += val

                val //= 3

            else : # empty stack or (...]
                return 0

    return total if not stack else 0


# input
ps = input()

#solution
print(solution(ps))