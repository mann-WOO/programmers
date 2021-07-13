# 조합을 생성하는 함수
def get_combination(combination, k, n, combinations, order_list):
    # 마지막 원소까지 확인 했다면
    if k == n:
        # 현재의 문자열 조합을 오름차순으로 정렬
        temp = list(combination)
        temp.sort()
        # 조합 리스트에 문자열을 추가
        combinations.append(''.join(temp))
    # 마지막 원소까지 확인 한 상태가 아니라면
    else:
        # 현재 원소를 추가하거나 추가하지 않고 다음 원소 확인
        get_combination(combination, k+1, n, combinations, order_list)
        get_combination(combination+order_list[k], k+1, n, combinations, order_list)


def solution(orders, course):
    answer = []
    # 각 조합의 등장 횟수를 셀 딕셔너리
    combination_count = {}
    # 각 주문들에 대해
    for order in orders:
        # 주문을 리스트로 변환
        order_list = list(order)
        # 주문에서 만들 수 있는 조합 모두 만들기
        combinations = []
        get_combination('', 0, len(order), combinations, order_list)
        # 생성된 조합을 확인하며
        for combination in combinations:
            # 딕셔너리에 있다면 값에 1을 합산
            if combination_count.get(combination):
                combination_count[combination] += 1
            # 딕셔너리에 없다면 초기화
            else:
                combination_count[combination] = 1
    # 코스요리 길이 별로
    for num in course:
        # 가장 선호하는 조합을 찾기 위한 스택과 most_freq
        stack = []
        most_freq = 0
        # 딕셔너리를 순회하며
        for key in combination_count.keys():
            # 딕셔너리의 키값(메뉴조합)의 길이가 코스요리 길이와 같고, 해당 조합이 2번 이상 등장했을 때
            if len(key) == num and combination_count[key] >= 2:
                # 현재 가장 선호하는 조합보다 더 자주 등장했다면 스택을 비우고 추가
                if combination_count[key] > most_freq:
                    most_freq = combination_count[key]
                    stack = []
                    stack.append(key)
                # 현재 가장 선호하는 조합과 같은 선호라면 스택에 추가
                elif combination_count[key] == most_freq:
                    stack.append(key)
        # 정답 리스트에 스택의 원소들을 추가
        answer.extend(stack)
    # 오름차순으로 정리하여 반환
    answer.sort()
    print(combination_count)
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))