def print_borad(borad):
    for row in borad:
        print(' | '.join(row))
        print('-'*9)

def check_winner(borad, player):
    for i in range(3):
        if all(borad[i][j] == player for j in range(3)) or all(borad[j][i] == player for j in range(3)):
            return True
        
        if all (borad[i][i] == player for i in range(3)) or all(borad[i][i-2] == player for i in range(3)):
            return True
        return False
    
def is_full(borad):
    return all(cell != ' ' for row in borad for cell in row)

def main():
    borad = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_borad(borad)
        row = int(input(f'Player {player}, enter the row (0, 1, 2): '))
        col = int(input(f'Player {player}, enter the colum (0, 1, 2): '))

        if 0 <= row < 3 and 0 <= col < 3 and borad[row][col] == ' ':
            borad[row][col] = player

            if check_winner(borad, player):
                print_borad(borad)
                print(f'Player {player} Wins')
                break

            if is_full(borad):
                print_borad(borad)
                print('This Game is Draw')
                break

            player = 'O' if player == 'X' else 'X'
        
        else:
            print('Invalid move, Try Again.')

if __name__ == '__main__':
    main()