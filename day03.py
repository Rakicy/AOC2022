def get_input(file_name):
    with open(file_name, 'r') as f:
        data = f.read().splitlines()
    return data

def part_one(data):
    letter_priority = letter_values()
    total_priority = 0
    for rucksack in data:
        half_item_count = int(len(rucksack)/2)
        compartment_one = rucksack[:half_item_count]
        compartment_two = rucksack[half_item_count:]
        matches = set()
        for item in compartment_one:
            if item in compartment_two:
                matches.add(item)
        for match in matches:
            total_priority += letter_priority[match]
    return total_priority
    

def letter_values():
    letters = dict()
    for letter_value in range(ord('a'),ord('z')+1):
        # subtract 96 to make a=1, b=2, etc.
        letters[chr(letter_value)] = letter_value - 96
    for letter_value in range(ord('A'),ord('Z')+1):
        # subtract 64 and add 26 to make A=27, B=28, etc.
        letters[chr(letter_value)] = letter_value - 64 + 26
    return letters

def part_two(data):
    badge_sum = 0
    letter_priority = letter_values()
    for group in chunker(data, 3):
        badge_sum += letter_priority[find_badge(group)]
    return badge_sum
    
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def find_badge(group):
    return (set(group[0]) & set(group[1]) & set(group[2])).pop()

def main():
    file_name = r"Advent of Code\2022\day03.txt"
    data = get_input(file_name)
    print(f"The answer to part one is {part_one(data)}")
    print(f"The answer to part two is {part_two(data)}")

if __name__ == "__main__":
    main()