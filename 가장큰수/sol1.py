# 오답
def solution(numbers):
    # 가장 긴 자릿수의 숫자의 길이 찾기
    max_value = max(numbers)
    max_len = len(str(max_value))
    # 가장 긴 숫자보다 짧은 숫자는 남은 자릿수를 해당 수의 가장 앞자리로 채워서 비교용 숫자 만들기
    tuple_numbers = []
    for number in numbers:
        str_number = str(number)
        compare_number = str_number
        if len(str_number) < max_len:
            for _ in range(max_len - len(str_number)):
                compare_number += str_number[0]
            tuple_numbers.append((str_number, compare_number))
        else:
            tuple_numbers.append((str_number, compare_number))

    # 비교용 숫자를 기준으로 정렬하기
    tuple_numbers.sort(reverse=True, key=lambda x: x[1])
    print(tuple_numbers)

    # 정렬된 숫자 리스트로 정답 스트링 만들어 반환하기
    answer = ''
    for number in tuple_numbers:
        answer += number[0]
    return answer


print(solution([3, 30, 34, 5, 9, 555, 69, 77, 80, 0, 341, 56, 9899]))
print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))

# 위 방법의 예외 케이스
print(solution([90,908,89,898,10,101,1,8,9]))

