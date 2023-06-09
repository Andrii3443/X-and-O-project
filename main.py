# Відображення ігрової дошки
def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Перевірка переможця
def check_winner(board, player):
    # Перевірка горизонтальних ліній
    if (board[0] == board[1] == board[2] == player) or \
       (board[3] == board[4] == board[5] == player) or \
       (board[6] == board[7] == board[8] == player):
        return True

    # Перевірка вертикальних ліній
    if (board[0] == board[3] == board[6] == player) or \
       (board[1] == board[4] == board[7] == player) or \
       (board[2] == board[5] == board[8] == player):
        return True

    # Перевірка діагоналей
    if (board[0] == board[4] == board[8] == player) or \
       (board[2] == board[4] == board[6] == player):
        return True

    return False

# Основна функція гри
def play_game():
    board = [' ' for _ in range(9)]  # Створення початкової пустої дошки
    current_player = 'X'  # Початковий гравець

    while True:
        display_board(board)  # Відображення поточного стану дошки

        position = int(input("Оберіть позицію (1-9): ")) - 1

        # Перевірка, чи позиція вільна
        if board[position] == ' ':
            board[position] = current_player

            # Перевірка переможця
            if check_winner(board, current_player):
                display_board(board)
                print("Гравець", current_player, "переміг!")
                break

            # Перевід ходу до наступного гравця
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Позиція вже зайнята. Оберіть іншу позицію.")

        # Перевірка на нічию
        if ' ' not in board:
            display_board(board)
            print("Нічия!")
            break

# Запуск гри
play_game()
