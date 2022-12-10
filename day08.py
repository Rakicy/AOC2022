import time
import numpy as np
def get_input(file_name):
    with open(file_name, 'r') as f:
        data = [[int(character) for character in line]for line in f.read().splitlines()]
        data = np.array(data)
    return data

def part_one(data):
    visible = np.zeros((len(data),len(data[0])),dtype=int)
    tally = 0
    reverse_tally = 0
    for col in range(len(data)):
        for row in range(len(data[0])):
            north = data[:row, col]
            south = data[row+1:, col]
            east = data[row, col+1:]
            west = data[row, :col]
            current_position = data[row][col]
            if is_visible(current_position, north):
                visible[row][col] = 1
                tally += 1
                continue
            if is_visible(current_position, east):
                visible[row][col] = 1
                tally += 1
                continue
            if is_visible(current_position, south):
                visible[row][col] = 1
                tally += 1
                continue
            if is_visible(current_position, west):
                visible[row][col] = 1
                tally += 1
                continue
            reverse_tally += 1
    return visible.sum()

def is_visible(number, num_list):
    if len(num_list) > 0:
        for num in num_list:
            if num >= number:
                return False
    return True

def part_two(data):
    trees_vis = np.zeros((len(data),len(data[0])),dtype=int)
    for col in range(len(data)):
        for row in range(len(data[0])):
            north = data[:row, col]
            north = np.flip(north)
            south = data[row+1:, col]
            east = data[row, col+1:]
            west = data[row, :col]
            west = np.flip(west)
            cur_pos = data[row][col]
            n_vis = trees_visible(cur_pos,north)
            s_vis = trees_visible(cur_pos,south)
            e_vis = trees_visible(cur_pos,east)
            w_vis = trees_visible(cur_pos,west)
            trees_vis[row][col] = n_vis*s_vis*e_vis*w_vis
    return trees_vis.max()

def trees_visible(number,num_list):
    if len(num_list) > 0:
        tree_count = 0
        for num in num_list:
            if num < number:
                tree_count += 1
            if num >= number:
                tree_count += 1
                return tree_count
        return tree_count
    return 0

def main():
    file_name = r"Advent of Code\2022\day08.txt"
    data = get_input(file_name)
    start = time.time()
    print(f"The answer to part one is {part_one(data)}")
    print(f"calculated in {time.time()-start}")
    start = time.time()
    print(f"The answer to part two is {part_two(data)}")
    print(f"calculated in {time.time()-start}")

if __name__ == "__main__":
    main()