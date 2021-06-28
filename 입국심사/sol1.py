# 답안 참조한 풀이
def solution(n, times):
    times.sort()
    # 가장 오래 걸리는 사람이 모두 처리할 때의 시간 r
    r = times[-1] * n
    l = 1
    # 이분탐색
    while l < r:
        # 중앙 설정
        mid = (r + l) // 2
        possible_people = 0
        # 중앙값의 시간동안 통과할 수 있는 사람 수 세기
        for time in times:
            possible_people += mid // time
        # 통과할 수 있는 사람수가 n명 이상이라면 오른쪽 끝점을 중앙값으로
        if possible_people >= n:
            r = mid
        # 통과할 수 잇는 사람수가 n명보다 적다면 왼쪽 끝점 + 1 을 중앙값으로
        else:
            l = mid + 1
    answer = l
    return answer


print(solution(6, [7, 10]))