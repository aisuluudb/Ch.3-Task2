# team1 = int(input("1 - Rock, 2 - Scissors, 3 - Paper"))
# team2 = int(input("1 - Rock, 2 - Scissors, 3 - Paper"))
counter_team1 = 0
counter_team2 = 0

while True:
    team1 = int(input("1 - Rock, 2 - Scissors, 3 - Paper"))
    team2 = int(input("1 - Rock, 2 - Scissors, 3 - Paper"))

    if team1 == 1 and team2 == 2:
        print("Team 1 won!")
        counter_team1 +=1
    elif team1 == 2 and team2 == 3:
        print("Team 2 won!")
        counter_team2 +=1
    elif team1 == 3 and team2 == 1:
        print("Team 1 won!")
        counter_team1 +=1
    elif team1 == 3 and team2 == 2:
        print("Team 2 won!")
        counter_team2 +=1
    elif team1 == 2 and team2 == 1:
        print("Team 2 won!")
        counter_team2 +=1
    elif team1 == 3 and team2 ==2:
        print("Team 1 won!")
        counter_team1 +=1
    elif team1 == 1 and team2 == 3:
        print("Team 2 won!")
        counter_team2 +=1
    else:
        print("nichya")
    if counter_team1 == 3 or counter_team2 == 3:
        print(counter_team1)
        print(counter_team2)
        break





