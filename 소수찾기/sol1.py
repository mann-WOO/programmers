# 시간초과
def solution(numbers):
    answer = 0
    # 해당 자릿수의 소수 리스트 만들기
    max_num = '9' * len(numbers)
    nums_array = [i for i in range(3, int(max_num)+1, 2)]
    prime_numbers = [2]
    while nums_array:
        prime = nums_array[0]
        prime_numbers.append(prime)
        temp_array = []
        for num in nums_array:
            if num % prime:
                temp_array.append(num)
        nums_array = temp_array

    # 카드의 숫자 빈도 세기
    count = [0 for _ in range(10)]
    for number in numbers:
        count[int(number)] += 1

    # 각 소수의 구성 숫자를 비교하며 가능한 경우 찾기
    for prime in prime_numbers:
        status = True
        for i in range(10):
            freq = str(prime).count(str(i))
            if count[i] < freq:
                status = False
                break
        if status:
            answer += 1

    return answer


print(solution('01234'))
