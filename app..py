import random

def generate_secret_number():
    digits = [random.randint(0, 9) for _ in range(4)]
    return digits

def check_guess(secret_number, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows

def play_game():
    print("Добро пожаловать в быков и коров! Введите 'play', чтобы начать игру, и 'exit', чтобы выйти из игры.欢迎来到bulls and cows!输入'play'开始游戏,输入'exit'退出游戏")
    command=input()
    if command=='exit':
        print("Вы отказались от участия в игре,你选择了退出游戏。")
        return
    elif command!= 'play':
        print("Если ввод неверный, введите «играть», чтобы начать игру, или «выход», чтобы выйти из игры.无效输入请输入'play'开始游戏或者'exit'退出游戏")
        play_game()
        return
    secret_number = generate_secret_number()
    player_turn = False
    game_over = False
    while not game_over:
        if player_turn:
            guess = input("Пожалуйста, введите свое предположение (четыре цифры, повторяющиеся,请输入你的猜测（四位数字，可重复）：")
            try:
                guess = [int(digit) for digit in guess]
                if len(guess)!= 4:
                    raise ValueError
            except ValueError:
                print("Ввод неверный, введите четыре цифры,输入无效，请输入四位数字。")
                continue
            bulls, cows = check_guess(secret_number, guess)
            print(f"有 {cows} 头奶牛和 {bulls} 头公牛。")
            if bulls == 4:
                print("winner,你猜对了！")
                game_over = True
        else:
            # 这里可以添加电脑猜测的逻辑，为了简单起见，先随机生成一个猜测
            guess = generate_secret_number()
            bulls, cows = check_guess(secret_number, guess)
            print(f"电脑猜测：{''.join(map(str, guess))}，有 {cows} 头奶牛和 {bulls} 头公牛。")
            if bulls == 4:
                print("winner,电脑猜对了！")
                game_over = True
        player_turn = not player_turn

    print("game over游戏结束。")

play_game()