def solution(board, moves):

    positionArray = [-1] * len(board[0])
    stack = []
    count = 0

    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[j][i] != 0 and positionArray[i] == -1:
                positionArray[i] = j

    for i in moves:

        i -= 1

        if positionArray[i] == (len(board) - 1) and board[positionArray[i]][i] == 0:
            continue

        if len(stack) > 0 and stack[-1] == board[positionArray[i]][i]:
            stack.pop()
            count += 2
        else:
            stack.append(board[positionArray[i]][i])

        board[positionArray[i]][i] = 0
        if positionArray[i] != (len(board) - 1):
            positionArray[i] += 1

    return count