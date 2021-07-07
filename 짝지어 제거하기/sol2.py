# replace 함수의 안좋은 효율성을 고려
def solution(s):
    # 짝이 없는 글자를 쌓을 스택
    stack = []
    # 모든 글자를 순회
    for i in range(len(s)):
        # 스택이 비었다면 스택에 현재 글자 추가
        if not stack:
            stack.append(s[i])
        # 스택에 글자가 있다면 스택의 마지막과 현재 글자 비교
        else:
            # 같다면 스택에서 하나 꺼내기
            if stack[-1] == s[i]:
                stack.pop()
            # 다르다면 스택에 현재 글자 추가
            else:
                stack.append(s[i])
    # 스택에 남은 글자가 있다면 실패
    if stack:
        return 0
    # 스택이 비었다면 성공
    else:
        return 1


print(solution('baabaa'))
print(solution('cdcd'))
print(solution('bbbaaaabaa'))