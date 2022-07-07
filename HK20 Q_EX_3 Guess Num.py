n = 17
attend = 1
RemainingAttempt = 8
print("Guess the number Under 30 ")

while attend <= 8:
    ges = int(input())

    if n < ges:
        print("This is greater then rite ans")
        print("You have ", RemainingAttempt - attend, "attempt left")

    elif n == ges:
        print("You take ", attend, "attend")
        print("This is the rite ans")
        break

    else:
        print("This is lesser then rite number")
        print("You have ", RemainingAttempt - attend, "attempt left")

    attend = attend + 1

if attend == 9:
    print("Game over")
else:
    print("You win")
