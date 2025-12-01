import math

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]


def replace_step(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b')


def solution(m, musicinfos):
    answer = None
    max_play_time = -1
    m = replace_step(m)

    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(",")
        play_time = (int(end_time[:2]) * 60 + int(end_time[3:])) - (int(start_time[:2]) * 60 + int(start_time[3:]))

        melody = replace_step(melody)
        melody_repeated_count = math.ceil(play_time/ len(melody))
        melody_played = (melody * melody_repeated_count)[:play_time]

        if m in melody_played:
            if play_time > max_play_time:
                answer = title
                max_play_time = play_time
            elif play_time == max_play_time and answer is None:
                answer = title

    if answer is None:
        return "(None)"

    return answer

print(solution(m, musicinfos))