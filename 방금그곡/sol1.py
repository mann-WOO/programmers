# 너무 복잡하게 풀었음
# A#, B# 을 a, b로 변환해서 하면 더 쉬웠을 것


def solution(m, musicinfos):
    # 정답의 기본값은 None, 정답 재생된 멜로디 길이 0으로 초기화
    answer = '(None)'
    answer_played_len = 0
    # 재생된 노래를 하나씩 확인
    for i in range(len(musicinfos)):
        start, end, title, melody = musicinfos[i].split(',')

        # 재생된 멜로디의 길이 계산
        start_hour = int(start.split(':')[0])
        start_min = int(start.split(':')[1])
        end_hour = int(end.split(':')[0])
        end_min = int(end.split(':')[1])
        # 재생된 멜로디의 시간 = (끝 시-시작 시)*60 + (끝 분 - 시작 분)
        melody_len = (end_hour-start_hour)*60 + (end_min-start_min)
        played_len = melody_len

        # 재생된 멜로디 문자열 만들기
        played_melody = ''
        # 포인터를 0에서 시작
        pointer = 0
        # 재생된 시간이 0이 될 때까지 1씩 빼줌
        while melody_len:
            # 현재 포인터가 #을 가리키고 있다면 1 안빼줌
            if melody[pointer] != '#':
                melody_len -= 1
            # 현재 포인터가 가리키는 문자열을 재생된 멜로디에 추가
            played_melody += melody[pointer]
            # 포인터가 마지막 위치라면 0으로 다시 보내기
            if pointer == len(melody) - 1:
                pointer = 0
            else:
                pointer += 1
        # 알파벳으로 끝나서 마지막 '#'이 안들어갔을 가능성? -> 이거땜에 오래걸림 예외처리가 너무 많다.
        if melody[pointer] == '#':
            played_melody += '#'

        # 일치하는 노래인지 확인
        if len(played_melody) - len(m) >= 0:
            # 한 칸씩 이동하며 문자열 확인
            for i in range(len(played_melody) - len(m) + 1):
                # 문자열이 주어진 문자열과 일치하고, 확인중인 문자열이 마지막이거나 뒤에 #이 없을 때
                if played_melody[i:i+len(m)] == m and (i+len(m) == len(played_melody) or played_melody[i+len(m)] != '#'):
                    # 현재 최대길이 정답 문자열과 비교해 갱신
                    if played_len > answer_played_len:
                        answer = title
                        answer_played_len = played_len
                    # 현재 문자열은 한 번만 확인하면 된다. break
                    break

    return answer


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))