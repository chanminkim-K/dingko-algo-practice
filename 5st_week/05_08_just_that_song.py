m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# "HELLO" 가 출력되어야 합니다.


def solution(m, musicinfos):
    answer = ''
    music_info = []
    correct_music = []

    for info in musicinfos:
        parts = info.split(',')
        music_info.append(parts)

    for i in range(len(music_info)):
        play_music = ""
        playing_time = int(musicinfos[i][9:11]) - int(musicinfos[i][3:5])

        if playing_time > len(music_info[i][3]):
            for time in range(playing_time):
                if time >= len(music_info[i][3]):
                    replay_time = time % len(music_info[i][3])
                else:
                    replay_time = time
                play_music += (music_info[i][3][replay_time])
        else:
            for time in range(playing_time):
                play_music += (music_info[i][3][time])

        if m in play_music:
            correct_music.append(music_info[i])

    if len(correct_music) > 1:
        max_title_length = 0
        for music in correct_music:
            if len(music[2]) > max_title_length:
                max_title_length = len(music[2])
                answer = music[2]
    else:
        answer = correct_music[0][2]

    return answer

print(solution(m, musicinfos))