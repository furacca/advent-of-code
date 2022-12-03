# ==========================
# 2022-12-01 - DAY ONE
# ==========================
# Calorie Counting
# ==========================
# https://adventofcode.com/2022/day/1
# ==========================
# 
# FIRST PART
# 
# Find the elf with the eighest number of calories inside their inventory

elf_inventory_list = []

with open("Input_files_2022_12_01.txt", "r") as day01file:
    lines = day01file.readlines()
    
    temp_elf_inventory = 0
    
    for x in lines:
        if x == "\n":
            elf_inventory_list.append(temp_elf_inventory)
            temp_elf_inventory = 0
        else:
            temp_elf_inventory += int(x)

elf_inventory_list.sort(reverse=True)

print(f"The highest number of calories carried is {elf_inventory_list[0]}")

# Answer: 70374

# ==========================
# 2022-12-01 - DAY ONE
# ==========================
# Calorie Counting
# ==========================
# https://adventofcode.com/2022/day/1
# ==========================
#
# SECOND PART

# Easiest way
# top_three_elf_calories_inventories = elf_inventory_list[0] + elf_inventory_list[1] + elf_inventory_list[2]


# Scalable way
top_x_elf_calories_inventories  = 0

number_of_inventory_elf_top_ranked_to_analyzed = 3

for x in range (0, number_of_inventory_elf_top_ranked_to_analyzed):
    top_x_elf_calories_inventories += elf_inventory_list[x]

print(f"The top {number_of_inventory_elf_top_ranked_to_analyzed} carry a total of {top_x_elf_calories_inventories} calories.")
#Answer: 204610