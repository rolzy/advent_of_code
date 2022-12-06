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

elif DAY == '2':
    print('Solving for DAY 2')
    with open(INPUT_FILE, 'r') as f:
        text_input = f.readlines()

    hand_dict = {'A':'rock', 'B':'paper', 'C':'scissors', 
                 'X':'rock', 'Y':'paper', 'Z':'scissors'}
    score_dict = {'rock': 1, 'paper': 2, 'scissors': 3, 
                  'lose': 0, 'draw': 3, 'win': 6}

    def rps(hand1, hand2):
        if hand1 == 'rock':
            if hand2 == 'rock':
                return 'draw'
            elif hand2 == 'paper':
                return 'win'
            elif hand2 == 'scissors':
                return 'lose'
        elif hand1 == 'paper':
            if hand2 == 'rock':
                return 'lose'
            elif hand2 == 'paper':
                return 'draw'
            elif hand2 == 'scissors':
                return 'win'
        elif hand1 == 'scissors':
            if hand2 == 'rock':
                return 'win'
            elif hand2 == 'paper':
                return 'lose'
            elif hand2 == 'scissors':
                return 'draw'

    def rigged_rps(hand1, hand2):
        if hand1 == 'rock':
            if hand2 == 'X':
                return ('lose', 'scissors')
            elif hand2 == 'Y':
                return ('draw', 'rock')
            elif hand2 == 'Z':
                return ('win', 'paper')
        elif hand1 == 'paper':
            if hand2 == 'X':
                return ('lose', 'rock')
            elif hand2 == 'Y':
                return ('draw', 'paper')
            elif hand2 == 'Z':
                return ('win', 'scissors')
        elif hand1 == 'scissors':
            if hand2 == 'X':
                return ('lose', 'paper')
            elif hand2 == 'Y':
                return ('draw', 'scissors')
            elif hand2 == 'Z':
                return ('win', 'rock')

    total_score = 0
    rigged_total_score = 0
    for line in text_input:
        line = line.strip()
        player1_input = line.split(' ')[0]
        player2_input = line.split(' ')[1]
        player1_hand = hand_dict.get(player1_input)
        player2_hand = hand_dict.get(player2_input)
        result = rps(player1_hand, player2_hand)
        score = score_dict.get(result) + score_dict.get(player2_hand)
        total_score += score

        rigged_result, rigged_hand = rigged_rps(player1_hand, player2_input)
        rigged_score = score_dict.get(rigged_result) + score_dict.get(rigged_hand)
        rigged_total_score += rigged_score


    print(f'Total score for first part: {total_score}')
    print(f'Total score for second part: {rigged_total_score}')

elif DAY == '3':
    print('Solving for DAY 3')

    def get_score(letter: str):
        if letter.isupper():
            return ord(letter)-38
        else:
            return ord(letter)-96

    with open(INPUT_FILE, 'r') as f:
        text_input = f.readlines()

    priority_sum = 0
    badge_sum = 0
    group_lines = []
    for line in text_input:
        line = line.strip()
        assert len(line) % 2 == 0
        group_lines.append(line)
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        shared_char = ''.join(set(first_half).intersection(second_half))
        assert len(shared_char) == 1
        score = get_score(shared_char)
        assert 1<=score<=52
        priority_sum += score
        if len(group_lines) == 3:
            badge_char = ''.join(set.intersection(*map(set, group_lines)))
            assert len(shared_char) == 1
            score = get_score(badge_char)
            assert 1<=score<=52
            badge_sum += score
            group_lines = []

    print(f'The sum of priorities is {priority_sum}')
    print(f'The sum of badges is {badge_sum}')

elif DAY == '4':
    print('Solving for DAY 4')

    with open(INPUT_FILE, 'r') as f:
        text_input = f.readlines()

    overlap_count = 0
    any_overlap_count = 0
    for line in text_input:
        line = line.strip()
        elf1_range = line.split(',')[0]
        elf2_range = line.split(',')[1]
        
        elf1_min = int(elf1_range.split('-')[0])
        elf1_max = int(elf1_range.split('-')[1])
        elf2_min = int(elf2_range.split('-')[0])
        elf2_max = int(elf2_range.split('-')[1])

        if (elf1_min <= elf2_min and elf1_max >= elf2_max) or \
                (elf2_min <= elf1_min and elf2_max >= elf1_max):
            overlap_count += 1
            any_overlap_count += 1
        elif (elf2_max >= elf1_max >= elf2_min) or \
                (elf1_max >= elf2_max >= elf1_min):
            any_overlap_count += 1

    print(f'There are {overlap_count} overlaps')
    print(f'There are {any_overlap_count} any-overlaps')

elif DAY == '5':
    print('Solving for DAY 5')

    with open(INPUT_FILE, 'r') as f:
        text_input = f.readlines()

    break_index = text_input.index('\n')
    initial_stack = text_input[:break_index]
    operations = text_input[break_index+1:]

    stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9:[]}
    for line in initial_stack:
        line = line.strip()
        stack = 1
        skip_counter = 0
        for char in line.split(' '):
            if '[' in char:
                stacks[stack].append(char.replace('[', '').replace(']', ''))
                stack += 1
            elif char == '':
                skip_counter += 1
                if skip_counter == 4:
                    stack += 1
                    skip_counter = 0
            else:
                break

    #PART 1
    #for line in operations:
    #    quantity = int(line.split(' ')[1])
    #    origin = int(line.split(' ')[3])
    #    destination = int(line.split(' ')[5])

    #    for i in range(quantity):
    #        stack = stacks.get(origin).pop(0)
    #        stacks.get(destination).insert(0, stack)
    #    for key, value in stacks.items():
    #        print(f'{key}: {value}')

    #PART 2
    for line in operations:
        quantity = int(line.split(' ')[1])
        origin = int(line.split(' ')[3])
        destination = int(line.split(' ')[5])

        stack = stacks.get(origin)[:quantity]
        stacks[destination] = stack + stacks.get(destination)
        stacks[origin] = stacks[origin][quantity:]
