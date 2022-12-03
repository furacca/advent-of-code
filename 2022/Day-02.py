# ==========================
# 2022-12-02 - DAY TWO
# ==========================
# Rock Paper Scissors
# ==========================
# https://adventofcode.com/2022/day/2
# ==========================
# 
# FIRST PART
# 

def whosthewinner(yourchoice,mychoice):
    round_result = 0

    if mychoice == "Rock":
        round_result += 1
        if yourchoice == "Rock":
            round_result += 3
        elif yourchoice == "Paper":
            round_result += 0
        elif yourchoice == "Scissors":
            round_result += 6
    elif mychoice == "Paper":
        round_result += 2
        if yourchoice == "Rock":
            round_result += 6
        elif yourchoice == "Paper":
            round_result += 3
        elif yourchoice == "Scissors":
            round_result += 0
    elif mychoice == "Scissors":
        round_result += 3
        if yourchoice == "Rock":
            round_result += 0
        elif yourchoice == "Paper":
            round_result += 6
        elif yourchoice == "Scissors":
            round_result += 3
    return round_result


with open("2022_12_01_Day_02.txt", "r") as day02file:
    lines = day02file.readlines()
    total_score = 0
    for everylines in lines:
        yourchoice = everylines[0].replace("A", "Rock").replace("B", "Paper").replace("C", "Scissors")
        mychoice = everylines[2].replace("X", "Rock").replace("Y", "Paper").replace("Z", "Scissors")
        total_score += whosthewinner(yourchoice,mychoice)
           
print(f"The total score with this first strategy is {total_score}.")

# Answer: 14264


# ==========================
# 2022-12-02 - DAY TWO
# ==========================
# Rock Paper Scissors
# ==========================
# https://adventofcode.com/2022/day/2
# ==========================
#
# SECOND PART

def pointgained(yourchoice,destiny):
    round_result = 0
    
    if destiny == "lose":
        round_result += 0
        if yourchoice == "Rock":
            round_result += 3
        elif yourchoice == "Paper":
             round_result += 1
        elif yourchoice == "Scissors":
             round_result += 2
    
    elif destiny == "draw":
        round_result += 3
        if yourchoice == "Rock":
            round_result += 1
        elif yourchoice == "Paper":
             round_result += 2
        elif yourchoice == "Scissors":
             round_result += 3
                
    elif destiny == "win":
        round_result += 6
        if yourchoice == "Rock":
            round_result += 2
        elif yourchoice == "Paper":
             round_result += 3
        elif yourchoice == "Scissors":
             round_result += 1
                
    return round_result


with open("2022_12_01_Day_02.txt", "r") as day02file:
    lines = day02file.readlines()
    total_score = 0
    for everylines in lines:
        yourchoice = everylines[0].replace("A", "Rock").replace("B", "Paper").replace("C", "Scissors")
        destiny = everylines[2].replace("X", "lose").replace("Y", "draw").replace("Z", "win")
        
        total_score += pointgained(yourchoice,destiny)

print(f"The total score with this news strategy is {total_score}.")

#Answer: 12382

