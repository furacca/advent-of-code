# ==========================
# 2022-12-05 - DAY FIVE
# ==========================
# Supply Stacks
# ==========================
# https://adventofcode.com/2022/day/5
# ==========================
#
# FIRST AND SECOND PART (in the last rows there are two call for two different function which give two different result)
#

# Day 05 - Supply Stacks


with open("Input_files_2022_12_05.txt", "r") as day05file:
    lines = day05file.readlines()
    
    stack_pile = []
    
    
    firstparse = ""
    for everylines in lines:
        # Choose only the lines which start with square brackets
        if everylines[0] == "[":
            firstparse += f'''{everylines.replace("    ", " [0] ").replace(" ","")},'''
        else:
            pass
    
    
    temporary_stack_pile_reversed_to_be_splitted = firstparse.split(",")    
    temporary_stack_pile_reversed = []
    
    for everyrow in temporary_stack_pile_reversed_to_be_splitted:
            temp_row = []
            for everychar in everyrow:
                if everychar == "[" or everychar == "]" or everychar == "\n":
                    pass
                else:
                    temp_row.append(everychar)
            temporary_stack_pile_reversed.append(temp_row)

    # Counting how many column there are
    column_counter = len(temporary_stack_pile_reversed[0])
    
    stack_pile = []
    
    for everycolumn in range(0,column_counter):
        hereiam = []
        for everylist in temporary_stack_pile_reversed:
            if len(everylist) == 0:
                pass
            else:
                if everylist[everycolumn] == "0":
                    pass
                else:
                    hereiam.append(everylist[everycolumn])
        stack_pile.append(hereiam)
        
        

    list_of_all_moves = []
    
    for everylines in lines:
        if everylines[0:1] == "m":
            # Splitting the text in something like ['move', '8', 'from', '8', 'to', '5']
            splittedtext = everylines.split()
            # Adding a list of three digit (the three moves) in the list [list_of_all_moves]
            list_of_all_moves.append([int(splittedtext[1]), int(splittedtext[3]), int(splittedtext[5])])
            
            
    
    # First part

def first_part(stack_pile,list_of_all_moves):
    for everymove in list_of_all_moves:
        # Run the cycle for n times, where n is the quantity of stack moved (everymove[0])
        for n in range(0,everymove[0]):
            initial_column = stack_pile[everymove[1]-1]
    #     ['C', 'J', 'N', 'F', 'Q', 'V', 'R', 'W']
            final_column = stack_pile[everymove[2]-1]
        
        
            final_column.insert(0, initial_column[0])
            initial_column.pop(0)
            
    partoneresult = ""
    for everylist in stack_pile:
        partoneresult += everylist[0]
    return partoneresult
           

def second_part(stack_pile,list_of_all_moves):
    for everymove in list_of_all_moves:
        
        initial_column = stack_pile[everymove[1]-1]
        final_column = stack_pile[everymove[2]-1]

        temporary_list = []

        for n in range(0,everymove[0]):
            temporary_list.append(initial_column[n])

        for n in range(0,everymove[0]):
            initial_column.pop(0)

        stack_pile[everymove[2]-1] = temporary_list + final_column

    parttworesult = ""
    for everylist in stack_pile:
        parttworesult += everylist[0]
    return parttworesult


first_part_result = first_part(stack_pile,list_of_all_moves) 
print(f"The first result: {first_part_result}")
#Answer: FWNSHLDNZ

second_part_result = second_part(stack_pile,list_of_all_moves)
print(f"The second result: {second_part_result}")
#Answer: RNRGDNFQG
    