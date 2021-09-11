def get_bowling_score(s):
    additional_score_multiple_array = [0] * (len(s))
    answer = 0
    frame = 1
    try_count_at_frame = 0

    for i in range(len(s)):
        set_additional_score_multiple(additional_score_multiple_array, frame, i, s)
        frame, try_count_at_frame = set_frame_and_try_count_at_frame(frame, i, s, try_count_at_frame)
        answer += get_score(i, s) * (1 + additional_score_multiple_array[i])  # 점수 구하기 + 추가 점수 구하기
    return answer


def set_frame_and_try_count_at_frame(frame, i, s, try_count_at_frame):
    try_count_at_frame += 1  # 프레임 수 구하기 -> 추가 점수 구하기
    if s[i] == 'S' or try_count_at_frame == 2:  # 프레임 수 구하기 -> 추가 점수 구하기
        frame += 1  # 프레임 수 구하기 -> 추가 점수 구하기
        try_count_at_frame = 0  # 프레임 수 구하기 -> 추가 점수 구하기
    return frame, try_count_at_frame


def set_additional_score_multiple(additional_score_multiple_array, frame, i, s):
    if s[i] == 'S':
        if frame < 10:  # 추가 점수 구하기
            additional_score_multiple_array[i + 1] += 1  # 추가 점수 구하기
            additional_score_multiple_array[i + 2] += 1  # 추가 점수 구하기
    elif s[i] == 'P':
        if frame < 10:  # 추가 점수 구하기
            additional_score_multiple_array[i + 1] += 1  # 추가 점수 구하기


def get_score(i, s):
    if s[i] == 'S':
        score = 10  # 점수 구하기
    elif s[i] == '-':
        score = 0  # 점수 구하기
    elif s[i] == 'P':
        if s[i - 1] == '-':  # 점수 구하기
            score = 10  # 점수 구하기
        else:
            score = 10 - int(s[i - 1])  # 점수 구하기
    else:
        score = int(s[i])  # 점수 구하기
    return score


assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300