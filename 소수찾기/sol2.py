# 시간초과
def eratosthenes(n):
    # 2-1. 차집합 활용을 위해 집합(set) 활용
    prime = set(range(2, n+1))

    # 2-2. n까지의 숫자(num)를 순회하면서
    for num in range(2, n+1):
        # 2-3. 만약 num이 prime에 있으면,
        # num의 2배수부터 지우는데, 최댓값 // 2보다 커지는 순간 지울 게 없어짐
        if num > max(prime)//2:
            break
        # 2-4. num이 prime에 있으면
        if num in prime:
            # 2-5. num을 제외한 num의 배수 전체를 prime에서 빼기
            prime -= set(range(2*num, n+1, num))
    return list(prime)


def solution(numbers):
    answer = 0
    # 해당 자릿수의 소수 리스트 만들기
    max_num = '9' * len(numbers)
    prime_numbers = eratosthenes(int(max_num))

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


print(solution('17'))
print(solution('011'))

