# ==========================
# 2022-12-04 - DAY FOUR
# ==========================
# Camp Cleanup
# ==========================
# https://adventofcode.com/2022/day/4
# ==========================
#
# FIRST PART
#
# REQUEST: In how many assignment pairs does one range fully contain the other?

# Reading input file
with open("Input_files_2022_12_04.txt", "r") as day04file:
    lines = day04file.readlines()
    
    assignment_pairs_target = 0
    four_number_list = []

    # Extracting for every lines the four numbers in the two couples
    for everylines in lines:
        pair_list = everylines.replace("\n","").split(",")
        
        for everyrange in pair_list:
            everyrange_list = everyrange.split("-")
            low_number = int(everyrange_list[0])
            high_number = int(everyrange_list[1])
            four_number_list.append(low_number)
            four_number_list.append(high_number)
        
        # Changing the names to be human readable
        x1 = four_number_list[0]
        y1 = four_number_list[1]
        x2 = four_number_list[2]
        y2 = four_number_list[3]
        
        # Rules to identify a full overlap
        if x1 == x2:
            assignment_pairs_target += 1
        elif x1 > x2 and y1 <= y2:
            assignment_pairs_target += 1
        elif x1 < x2 and y1 >= y2:
            assignment_pairs_target += 1
        
        # Flush the list for the next cycle
        four_number_list = []
    
    print(f"There are {assignment_pairs_target} assignment pairs which **FULLY** contains the other.")
    
#Answer: 602

# ==========================
# 2022-12-04 - DAY FOUR
# ==========================
# Camp Cleanup
# ==========================
# https://adventofcode.com/2022/day/4
# 
# SECOND PART
# 
# REQUEST: In how many assignment pairs do the ranges overlap?


# Reading input file
with open("Input_files_2022_12_04.txt", "r") as day04file:
    lines = day04file.readlines()
    
    overlap_at_all = 0
    four_number_list = []

    # Extracting for every lines the four numbers in the two couples
    for everylines in lines:
        pair_list = everylines.replace("\n","").split(",")
        
        for everyrange in pair_list:
            everyrange_list = everyrange.split("-")
            low_number = int(everyrange_list[0])
            high_number = int(everyrange_list[1])
            
            four_number_list.append(low_number)
            four_number_list.append(high_number)
        
        # Changing the names to be human readable
        x1 = four_number_list[0]
        y1 = four_number_list[1]
        x2 = four_number_list[2]
        y2 = four_number_list[3]

        # Rules to identify a partial overlap
        if x1 == x2:
            overlap_at_all += 1
        elif x1 < x2 and x2 <= y1:
            overlap_at_all += 1
        elif x1 > x2 and x1 <= y2:
            overlap_at_all += 1
            
        # Flush the list for the next cycle
        four_number_list = []
        
    print(f"There are {overlap_at_all} assignment pairs which **PARTIAL** contains the other.")

#Answer: 891