def get_bowling_score(s):
    frame = 1  # 프레임 수 구하기 -> 추가 점수 구하기
    stack = 0  # 프레임 수 구하기 -> 추가 점수 구하기
    answer = 0  # 총 점수 구하기
    plus = []  # 추가 점수 구하기
    for i in range(len(s)):
        append_index_to_plus(frame, i, plus, s)
        frame, stack = set_frame_and_stack(frame, i, s, stack)

        answer += get_score(i, s) * (plus.count(i) + 1)  # 점수 구하기 + 추가 점수 구하기

    return answer


def set_frame_and_stack(frame, i, s, stack):
    if s[i] == 'S':
        stack = 0  # 프레임 수 구하기 -> 추가 점수 구하기
        frame += 1  # 프레임 수 구하기 -> 추가 점수 구하기
    else:
        stack += 1  # 프레임 수 구하기 -> 추가 점수 구하기
        if stack == 2:  # 프레임 수 구하기 -> 추가 점수 구하기
            stack = 0  # 프레임 수 구하기 -> 추가 점수 구하기
            frame += 1  # 프레임 수 구하기 -> 추가 점수 구하기
    return frame, stack


def append_index_to_plus(frame, i, plus, s):
    if s[i] == 'S':
        if frame < 10:  # 추가 점수 구하기
            plus.append(i + 1)  # 추가 점수 구하기
            plus.append(i + 2)  # 추가 점수 구하기
    elif s[i] == 'P':
        if frame < 10:  # 추가 점수 구하기
            plus.append(i + 1)  # 추가 점수 구하기


def get_score(i, s):
    if s[i] == 'S':
        add = 10  # 점수 구하기
    else:
        if s[i] == 'P':
            if s[i - 1] == '-':
                add = 10  # 점수 구하기
            else:
                add = 10 - int(s[i - 1])  # 점수 구하기
        elif s[i] == '-':  # 점수 구하기
            add = 0  # 점수 구하기
        else:  # 점수 구하기
            add = int(s[i])  # 점수 구하기
    return add


assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300