import time
import re
def get_input(file_name):
    with open(file_name, 'r') as f:
        data = [list(re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", line)[0]) for line in f.readlines()]
    data = [[int(number) for number in section] for section in data]
    return data

def part_one(data):
    tally = 0
    for group in data:
        elf_one = group[:2]
        elf_two = group[2:]
        if does_contain(elf_one, elf_two) or does_contain(elf_two, elf_one):
            tally += 1 
    return tally

def does_contain(first, second):
    return first[0] >= second[0] and first[1] <= second[1]

def part_two(data):
    tally = 0
    for group in data:
        elf_one = group[:2]
        elf_two = group[2:]
        if does_overlap(elf_one, elf_two):
            tally += 1
    return tally

def does_overlap(first, second):
    return first[0] <= second[1] and first[1] >= second[0]

def main():
    file_name = r"Advent of Code\2022\day04.txt"
    data = get_input(file_name)
    start = time.time()
    print(f"The answer to part one is {part_one(data)}")
    print(f"calculated in {time.time()-start}")
    start = time.time()
    print(f"The answer to part two is {part_two(data)}")
    print(f"calculated in {time.time()-start}")

if __name__ == "__main__":
    main()