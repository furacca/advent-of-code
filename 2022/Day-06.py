# ==========================
# 2022-12-06 - DAY SIX
# ==========================
# Tuning Trouble
# ==========================
# https://adventofcode.com/2022/day/6
# ==========================
#
# FIRST AND SECOND PART TOGETHER
# Just change the value of the variable "length_of_string"

with open("Input_files_2022_12_06.txt", "r") as file:
    lines = file.read()

signal_charstring = ""
length_of_string = 4
char_counter = 0

for x in range(0,len(lines)-length_of_string):
    signal_charstring = ""
    for n in range(0,length_of_string):
        signal_charstring += lines[n+x]
    thejobaredone = 0
    for everychar in signal_charstring:
        gnao = signal_charstring.count(everychar)
        if gnao != 1:
            thejobaredone = 1
    if thejobaredone == 1:
        pass
    else:
        print("")
        print(signal_charstring)
        print(char_counter + length_of_string)
        break
    char_counter += 1
    
    # Answer (first part): 1235
    # Answer (second part): 3051