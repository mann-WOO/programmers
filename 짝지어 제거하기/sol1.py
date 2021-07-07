# 효율성 테스트 시간초과
# replace 함수의 효율?
def solution(s):
    # 문자열 chars
    chars = s
    # 포인터 설정
    pointer = 0
    # 포인터의 위치가 검색가능한 구간인 동안에 반복
    while pointer <= len(chars) - 2:
        # 포인터의 글자와 포인터 다음 글자가 일치할 경우
        if chars[pointer] == chars[pointer+1]:
            # 반복되는 문자열을 공백으로 변환
            # 주의: replace 함수는 문자열을 수정하는게 아니라 수정된 문자열을 반환한다!
            target = chars[pointer]*2
            chars = chars.replace(target, '')
            # 포인터가 처음에 있지 않다면 한칸 앞으로 이동
            if pointer >= 1:
                pointer -= 1
        # 포인터의 글자가 연달아 나오는 글자가 아니라면 포인터를 한 칸 이동
        else:
            pointer += 1
    # 문자열이 공백이 아니라면 0 반환
    if chars:
        return 0
    # 문자열이 공백이라면 1반환
    else:
        return 1


print(solution('baabaa'))
print(solution('cdcd'))
print(solution('bbbaaaabaa'))