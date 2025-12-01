board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
# 4 가 출력되어야 합니다.

def solution(board, moves):
    answer = 0
    buket = []
    n = len(board[0])

    for move in moves:
        for i in range(n):
            doll = board[i][move - 1]
            if doll != 0:
                buket.append(doll)
                board[i][move - 1] = 0
                if len(buket) >= 2 and buket[-1] == buket[-2]:
                    buket = buket[:-2]
                    answer += 2
                break
    return answer

print(solution(board, moves))