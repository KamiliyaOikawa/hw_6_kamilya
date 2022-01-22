from fartune import Fortune
from logica import PlayCasino

cash = 1000
plus_or_minus = 0
print("Playing at the casino Choose a slot and bet")
while True:
    slot = int(input("Выберите слот: "))
    bid = int(input("Ваша ставка: "))
    play = PlayCasino(cash, plus_or_minus)
    play.game(slot, bid)
    plus_or_minus = play.plus_or_minus
    ret = input("Do you want to continue: yes/no ")
    if ret == "yes":
        continue
    else:
        if play.plus_or_minus > 0:
            print(f"You win {play.plus_or_minus}$")
        else:
            print(f"You've lost {play.plus_or_minus}$")
        a = input("Do you want to play Fortune? yes/no")# новая игра
        if a == "yes":
            print("Answer only I believe and I don't believe")
            play_2 = Fortune()
            play_2.game(play.plus_or_minus)
            cash += play_2.result
            print(f"Now you have {cash}$")
            break
        else:
            cash += play.plus_or_minus
            print(f"Now you have {cash}$")
            break
