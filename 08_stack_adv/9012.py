# https://www.acmicpc.net/problem/9012
# Check Balanced Parentheses - Stack
def check_vps(ps): # VPS 확인 함수

    st = [] # stack

    for pr in ps:

        if pr == ')' :
            if st :
                st.pop()
            else :
                return "NO"

        else:
            st.append("(")

    return "NO" if st else "YES"


def solution(PS):
    return "\n".join(check_vps(ps) for ps in PS) # 각 문자열마다 VPS 체크 후 결과 저장

# input
T = int(input())
PS = [input() for _ in range(T)]

# solution
ans = solution(PS)
print(ans)