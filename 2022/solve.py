import os
import sys

INPUT_FILE = sys.argv[1]
DAY = sys.argv[2]

assert os.path.isfile(INPUT_FILE)

if DAY == '1':
    print('Solving for DAY 1')

    elf_calories = {}
    calory = 0
    elf_id = 1
    with open(INPUT_FILE, 'r') as f:
        text_input = f.readlines()

    for line in text_input:
        if line != '\n':
            calory += int(line)
        else:
            print(f'Elf {elf_id} has {calory} calories.')
            elf_calories[elf_id] = calory
            elf_id += 1
            calory = 0

    max_key = max(elf_calories, key=elf_calories.get)
    print(f'Elf {max_key} has the most amount of calories with {elf_calories[max_key]}')

    top_3_keys = sorted(elf_calories, key=elf_calories.get, reverse=True)[:3]
    total_calories = sum([elf_calories.get(i) for i in top_3_keys])
    print(f'Elves {top_3_keys} have the most amount of calories with a total of {total_calories}')




        
