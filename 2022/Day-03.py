# ==========================
# 2022-12-03 - DAY THREE
# ==========================
# Rucksack Reorganization
# ==========================
# https://adventofcode.com/2022/day/3
# ==========================
#
# FIRST PART
#
# Every elf has a backpack with two large compartments.
# All items of a given type are meant to go into exactly one of the two compartments.
# The elf in charge to packing all the goods (the letters) failed to follow this rule for exactly one item per backpack.
# 
# Goal: find the good (letter) which is in both compartments


# Dict to save the correlation between letters and priorities
alphabet_upper_lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
priority_dict = {}
priority_number = 1
for everychar in alphabet_upper_lower:
    priority_dict[everychar] = priority_number
    priority_number += 1

# Reading input file
with open("Input_files_2022_12_03.txt", "r") as day03file:
    lines = day03file.readlines()

    # List of the wrong items (which are in both comparments)
    char_intruder = []
    
    for everylines in lines:
        temp_char = []
        for everychar in everylines:
            temp_char.append(everychar)
            
        # Removing the "\n" from every list
        temp_char.pop(-1)

        single_inventory_dimension = int(len(temp_char) / 2)
        
        first_half = temp_char[0:single_inventory_dimension]
        second_half = temp_char[single_inventory_dimension:]

        # Check every char in the first inventory with every char of the second inventory
        for everychar in first_half:
            if everychar in second_half:
                temp_char = everychar

        char_intruder.append(temp_char)
        
    # Using the priority_dict whe add every priority to sum_priorities
    sum_priorities = 0
    for everyelement in char_intruder:
        # print(everyelement)
        sum_priorities += priority_dict[everyelement]
    
    print(f"The sum of all the intruder's priority is equal to {sum_priorities}.")
    
#Answer: 8401

# ==========================
# 2022-12-03 - DAY THREE
# ==========================
# Rucksack Reorganization
# ==========================
# https://adventofcode.com/2022/day/3
# 
# SECOND PART
# 
# The Elves are divided into groups of three
# Every Elf carries a badge that identifies their group. 
# For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves.
# 
# Goal: find the badges (same letter in all backpack for every group of elf) (and calculate the total priority) 

# The dict with the correlation between letter and priority already exists -> alphabet_upper_lower


# Reading input file
with open("Input_files_2022_12_03.txt", "r") as day03file:
    lines = day03file.readlines()
    
    # List of lists (cointains 100 lists made by 3 lines each)
    lines_group = []
    
    # Temporary list (cointains 3 lines)
    group_of_three = []
    
    # Keeps track of how many lines are appended to the temporary list
    counter = 0
    
    # Avoid the skipping of the last lines_group
    linescounter = 0
    
    # Add to [group_of_three] list the [lines_group]
    for everylines in lines:
        if counter != 3 and linescounter == 299:
            group_of_three.append(everylines)
            lines_group.append(group_of_three)
        elif counter != 3:
            group_of_three.append(everylines)
            counter += 1
            linescounter += 1
        elif counter == 3:
            lines_group.append(group_of_three)
            group_of_three = []
            group_of_three.append(everylines)
            counter = 1
            linescounter += 1
    
    
    # Find for lists [lines_group] the char with the badge's role
    badge_list = []
    alreadyadded = 0
    for everylist in lines_group:
        alreadyadded = 0
        for everychar in everylist[0]:
            if everychar in everylist[1]:
                if everychar in everylist[2] and everychar != "\n" and alreadyadded == 0:
                    badge_list.append(everychar)
                    alreadyadded += 1
    
    
    
    # Using the priority_dict whe add every priority to sum_bagdes_priorities
    sum_bagdes_priorities = 0
    for everyelement in badge_list:
        sum_bagdes_priorities += priority_dict[everyelement]
        
    print(f"The sum of all the badges' priority is equal to {sum_bagdes_priorities}.")

#Answer: 2641