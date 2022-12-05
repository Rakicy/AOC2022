import time
import re
import numpy as np

def get_input(file_name):
    with open(file_name, 'r') as f:
        stacks, directions = f.read().split('\n\n')
    return parse_stacks(stacks), parse_directions(directions)

def parse_stacks(stacks):
    stacks = np.fliplr(np.transpose([list(level) for level in stacks.splitlines()]))
    clean_stacks = dict()
    for stack in stacks:
        location = stack[0]
        if not (location == ' '):
            trimmed_stack = [container for container in stack[1:] if not( container == ' ')]
            clean_stacks[int(location)] = trimmed_stack
    return clean_stacks

def parse_directions(directions):
    directions_str = [list(re.findall(r"(\d+).+(\d+).+(\d+)", direction)[0]) for direction in directions.splitlines()]
    return [[int(entry) for entry in direction] for direction in directions_str]

def part_one(data):
    stacks = data[0]
    directions = data[1]
    final_stacks = process_stacks(directions, stacks)
    return "".join(find_tops(final_stacks))

def find_tops(stacks):
    return [stacks[stack+1][-1:][0] for stack in range(len(stacks))]

def process_stacks(directions, stacks):
    for direction in directions:
        containers_to_move = direction[0]
        stack_from = direction[1]
        stack_to = direction[2]
        sub_stack = stacks[stack_from][-containers_to_move:]
        to_append = flip_list(sub_stack)
        stacks[stack_to] += to_append
        stacks[stack_from] = stacks[stack_from][:-containers_to_move]
    return stacks

def flip_list(flip_it):
    if len(flip_it) > 1:
        flip_it.reverse()
        return flip_it
    return flip_it

def part_two(data):
    stacks = data[0]
    directions = data[1]
    final_stacks = process_stacks_part_two(directions, stacks)
    return "".join(find_tops(final_stacks))

def process_stacks_part_two(directions, stacks):
    for direction in directions:
        containers_to_move = direction[0]
        stack_from = direction[1]
        stack_to = direction[2]
        sub_stack = stacks[stack_from][-containers_to_move:]
        # to_append = flip_list(sub_stack)
        to_append = sub_stack
        stacks[stack_to] += to_append
        stacks[stack_from] = stacks[stack_from][:-containers_to_move]
    return stacks

def main():
    file_name = r"Advent of Code\2022\day05.txt"
    data = get_input(file_name)
    start = time.time()
    print(f"The answer to part one is {part_one(data)}")
    print(f"calculated in {time.time()-start}")
    data = get_input(file_name)
    start = time.time()
    print(f"The answer to part two is {part_two(data)}")
    print(f"calculated in {time.time()-start}")

if __name__ == "__main__":
    main()