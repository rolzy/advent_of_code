import os
import sys
import math
from queue import PriorityQueue

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

elif DAY == '6':
    print('Solving for DAY 6')

    with open(INPUT_FILE, 'r') as f:
        text_input = f.read().strip()

    def unique(s):
        return len(set(s)) == len(s)

    for i in range(len(text_input)):
        packet_string = text_input[i:i+4]
        message_string = text_input[i:i+14]
        if unique(packet_string):
            print(f'The packet starts at {i+4}')
        if unique(message_string):
            print(f'The message starts at {i+14}')
            break

elif DAY == '7':
    print('Solving for DAY 7')

    with open(INPUT_FILE, 'r') as f:
        text_input = f.readlines()

    MAX_SIZE = 100000
    directories = {}

    def traverse(line_number, current_directory, depth):
        current_directory = current_directory + str(depth) # make the dir ID unique
        if directories.get(current_directory):
            i = 2
            while True:
                current_directory = current_directory + str(depth) + '_' + str(i)
                if not directories.get(current_directory):
                    break
                i += 1
        directories[current_directory] = 0
        while line_number < len(text_input):
            line = text_input[line_number].strip()
            line_number += 1
            if line[0] == '$':
                if 'cd' in line:
                    target_directory = line.split(' ')[2]
                    if target_directory == '..':
                        return line_number, directories.get(current_directory)
                    elif target_directory != '/':
                        line_number, child_dir_size = traverse(line_number, target_directory, depth+1)
                        directories[current_directory] += child_dir_size
            elif line.startswith('dir'):
                subdir_name = line.split(' ')[1]
            elif line[0].isdigit():
                file_size = line.split(' ')[0]
                directories[current_directory] += int(file_size)
            if line_number == len(text_input):
                return line_number, directories.get(current_directory)

    traverse(0, '/', 0)
    small_folder_sum = sum([i for i in directories.values() if i <= MAX_SIZE])
    print(f"The sum of small folders is {small_folder_sum}")

    TOTAL_DISK_SPACE=70_000_000
    REQUIRED_DISK_SPACE=30_000_000

    available_space = TOTAL_DISK_SPACE - directories['/0']
    space_to_delete = REQUIRED_DISK_SPACE - available_space
    sorted_directories = sorted(directories.items(), key=lambda x: x[1], reverse=True)
    min_ind = sorted_directories.index(min([i for i in sorted_directories if i[1] > space_to_delete], key=lambda tup: tup[1]))
    print(f'The size of the folder that will free up enough space is {sorted_directories[min_ind]}')

elif DAY == '8':
    print('Solving for DAY 8')

    with open(INPUT_FILE, 'r') as f:
        rows = f.readlines()

    rows = [[int(char) for char in list(row.strip())] for row in rows]
    columns = []

    for line in rows:
        for i, char in enumerate(line):
            try:
                columns[i].append(char)
            except IndexError:
                columns.append([char])


    def is_visible(row, col, row_ind, col_ind):
        height = row[col_ind]
        if all([height > tree for tree in row[:col_ind]]) or \
            all([height > tree for tree in row[col_ind+1:]]):
            return True
        elif all([height > tree for tree in col[:row_ind]]) or \
            all([height > tree for tree in col[row_ind+1:]]):
            return True
        return False

    def view_score(row, col, row_ind, col_ind):
        height = row[col_ind]
        left_trees = list(reversed(row[:col_ind]))
        right_trees = row[col_ind+1:]
        up_trees = list(reversed(col[:row_ind]))
        down_trees = col[row_ind+1:]

        left_score = next((i+1 for i, x in enumerate(left_trees) if x >= height), len(left_trees))
        right_score = next((i+1 for i, x in enumerate(right_trees) if x >= height), len(right_trees))
        up_score = next((i+1 for i, x in enumerate(up_trees) if x >= height), len(up_trees))
        down_score = next((i+1 for i, x in enumerate(down_trees) if x >= height), len(down_trees))

        return left_score * right_score * up_score * down_score

    visible = 0
    visibility_scores = []
    for i, row in enumerate(rows):
        for j, col in enumerate(columns):
            if is_visible(row, col, i, j):
                visible += 1
            visibility_scores.append(view_score(row, col, i, j))

    print(f'There are {visible} visible trees.')
    print(f'There best tree has a visibility score of {max(visibility_scores)}.')

elif DAY == '9':
    print('Solving for DAY 9')

    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y
            self.visited_points = [(x, y)]

        def __repr__(self):
            return f'({self.x}, {self.y})'

        def set_coords(self, delta_x: int, delta_y: int):
            self.x += delta_x
            self.y += delta_y

            if (self.x, self.y) not in self.visited_points:
                self.visited_points.append((self.x, self.y))


    class State:
        def __init__(self, rope):
            self.rope = rope

        def tail_needs_moving(self, tail_index):
            head = self.rope[tail_index - 1]
            tail = self.rope[tail_index]
            return (abs(head.x-tail.x)>1) or \
                (abs(head.y-tail.y)>1)

        def move_head(self, direction: str, distance: int):
            for _ in range(1, distance+1):
                multiplier = 1 if direction in ['R', 'U'] else -1
                if direction in ['L', 'R']:
                    delta_x = 1*multiplier
                    delta_y = 0
                elif direction in ['U', 'D']:
                    delta_x = 0
                    delta_y = 1*multiplier
                else:
                    sys.exit()

                self.rope[0].set_coords(delta_x, delta_y)

                for i, tail in enumerate(self.rope):
                    if i == 0:
                        continue
                    if self.tail_needs_moving(i):
                        self.move_tail(i)

        def move_tail(self, tail_index: int):
            head = self.rope[tail_index - 1]
            tail = self.rope[tail_index]
            sign = lambda x: (x>0) - (x<0)
            delta_x = head.x - tail.x
            delta_y = head.y - tail.y
            tail.set_coords(1*sign(delta_x), 1*sign(delta_y))
    
    # PART 1
    rope = [Point(0, 0) for _ in range(2)]
    state = State(rope)
    for line in lines:
        state.move_head(line.split(' ')[0], int(line.split(' ')[1]))
    print(f'Tail have visited {len(rope[-1].visited_points)} tiles')

    # PART 2
    rope = [Point(0, 0) for _ in range(10)]
    state = State(rope)
    for line in lines:
        state.move_head(line.split(' ')[0], int(line.split(' ')[1]))

    print(f'Tail have visited {len(rope[-1].visited_points)} tiles')

elif DAY == '10':
    print('Solving for DAY 10')

    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    class Device:
        def __init__(self):
            self.X = 1
            self.cycle = 0
            self.signal_strengths = []
            self.CRT_drawing = ['']

        def pixel(self):
            pixel_position = self.cycle - (40 * (len(self.CRT_drawing)-1))
            if pixel_position in [self.X-1, self.X, self.X+1]:
                return '#'
            else:
                return '.'

        def add_cycle(self):
            self.CRT_drawing[-1] += self.pixel() 
            self.cycle += 1
            if (self.cycle == 20) or ((self.cycle-20) % 40 == 0):
                self.signal_strengths.append(self.X * self.cycle)
            elif self.cycle % 40 == 0:
                self.CRT_drawing.append('')

        def add_x(self, x: int):
            self.X += x

    device = Device()
    for line in lines:
        command = line.split(' ')[0]
        if command == 'noop':
            device.add_cycle()
        elif command == 'addx':
            device.add_cycle()
            device.add_cycle()
            device.add_x(int(line.split(' ')[1]))

    print(f'The sum of signal strength is {sum(device.signal_strengths)}')
    for line in device.CRT_drawing:
        print(line)

elif DAY == '11':
    print('Solving for DAY 11')

    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    class Monkey:
        def __init__(self, items: list, operator: str, factor: str, modulo: int, 
                     true_target: int, false_target: int):
            self.item_list = items
            self.operator = operator
            self.factor = factor

            self.modulo = modulo

            self.true_target = true_target
            self.false_target = false_target

            self.inspect_count = 0

        def __repr__(self):
            return f"""
Item list: {self.item_list}
Inspection Operation: old {self.operator} {self.factor}
Test function: divisible by {self.modulo}
True target: {self.true_target}
False target: {self.false_target}
        """
        def add_item(self, item: int):
            self.item_list.append(item)

        def inspect_item(self, item: int) -> int:
            self.inspect_count += 1
            if self.factor == 'old':
                factor = item
            else:
                factor = int(self.factor)

            if self.operator == '+':
                item += factor
            elif self.operator == '*':
                item *= factor

            return item

        def test_item(self, item: int) -> bool:
            return True if item % self.modulo == 0 else False

    monkeys = []
    for line in lines:
        if 'Starting' in line:
            item_list = [int(x) for x in line.split(':')[1].replace(',', '').split(' ') if x]
        elif 'Operation' in line:
            operator = line.split(' ')[4]
            factor = line.split(' ')[5]
        elif 'Test' in line:
            modulo = int(line.split(' ')[3])
        elif 'If true' in line:
            true_target = int(line.split(' ')[5])
        elif 'If false' in line:
            false_target = int(line.split(' ')[5])
            monkeys.append(Monkey(item_list, operator, factor, modulo, true_target, false_target))

    for i, monkey in enumerate(monkeys):
        print(f'Monkey {i}')
        print(monkey)

    NUM_ROUNDS = 10000

    super_modulo = math.prod([m.modulo for m in monkeys])
    for i in range(NUM_ROUNDS):
        #print(f'Start round {i}')
        for i, monkey in enumerate(monkeys):
            #print(f'Monkey {i}')
            for item in list(monkey.item_list):
                #print(f'  Monkey inspects an item with a worry level of {item}.')
                item = monkey.inspect_item(item)
                #if monkey.operator == '+':
                    #print(f'    Worry level increases by {monkey.factor} to {item}.')
                #elif monkey.operator == '*':
                    #print(f'    Worry level is multiplied by {monkey.factor} to {item}.')
                #item = math.trunc(item/3)
                item = item % super_modulo
                #print(f'    Monkey gets bored with item. Worry level is divided by 3 to {item}')
                if monkey.test_item(item):
                    #print(f'    Current worry level is divisible by {monkey.modulo}.')
                    monkeys[monkey.true_target].add_item(item)
                    #print(f'    Item with worry level {item} is thrown to monkey {monkey.true_target}')
                else:
                    #print(f'    Current worry level is not divisible by {monkey.modulo}.')
                    monkeys[monkey.false_target].add_item(item)
                    #print(f'    Item with worry level {item} is thrown to monkey {monkey.false_target}')
                monkey.item_list.pop(0)

    for i, monkey in enumerate(monkeys):
        print(f'Monkey {i}: inspected items {monkey.inspect_count} times.')
    sorted_inspect_count = sorted([m.inspect_count for m in monkeys], reverse=True)
    print(f'Monkey shenanigans: {sorted_inspect_count[0] * sorted_inspect_count[1]}')

elif DAY == '12':
    print('Solving for DAY 12')

    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    class Graph:
        def __init__(self, lines: list):
            self.lines = lines
            self.set_coords(0, 0)

        def get_coords(self):
            return (self.x, self.y)

        def set_coords(self, coords: tuple):
            self.x = coords[0]
            self.y = coords[1]
            if lines[self.y][self.x] == 'S':
                self.altitude = 'a'
            else:
                self.altitude = lines[self.y][self.x]

        def get_neighbours(self): 
            possible_destinations = []
            if self.x-1 >= 0:
                possible_destinations.append((self.x-1, self.y)) 
            if self.x+1 < len(lines[self.y]): 
                possible_destinations.append((self.x+1, self.y)) 
            if self.y-1 >= 0: 
                possible_destinations.append((self.x, self.y-1)) 
            if self.y+1 < len(lines): 
                possible_destinations.append((self.x, self.y+1)) 

            for i, (new_x, new_y) in enumerate(list(possible_destinations)):
                if ord(self.lines[new_y][new_x]) - ord(self.altitude) > 1:
                    del possible_destinations[i]

            return possible_destinations

    class Astar:
        def __init__(self, graph: Graph):
            self.graph = graph
            self.frontier = PriorityQueue()
            self.frontier.put((0, self.graph.get_coords()))
            self.origins = {}
            self.origins[self.graph.get_coords()] = None
            self.costs = {}
            self.costs[self.graph.get_coords()] = 0

        def solve(self):
            while not self.frontier.empty():
                current = self.frontier.get()
                self.graph.set_coords(current)

                if self.graph.altitude == 'E':
                    break

                for neighbour in self.graph.get_neighbours():
                    new_cost = self.costs[current] + 1
                    if neighbour not in self.costs or new_cost < self.costs[neighbour]:
                        self.costs[neighbour] = new_cost

                break

    graph = Graph(lines)
    while True:
        print(f'I am currently at {(current_x, current_y)}. The altitude is {current_altitude}.')
        break


