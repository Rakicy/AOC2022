import time
def get_input(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
    return data

def part_one(data):
    offset = 4
    for count in range(len(data)-offset):
        sub_string = data[count:count+offset]
        if char_is_in_str(sub_string):
            return count+offset
    return 0

def char_is_in_str(sub_string):
    for letter in sub_string:
        if sub_string.count(letter) > 1:
            return False
    return True

def part_two(data):
    offset = 14
    for count in range(len(data)-offset):
        sub_string = data[count:count+offset]
        if char_is_in_str(sub_string):
            return count+offset
    return 0

def main():
    file_name = r"Advent of Code\2022\day06.txt"
    data = get_input(file_name)
    test1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
    test2 = 'nppdvjthqldpwncqszvftbrmjlhg'
    test3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
    test4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
    print(f'The answer to test1 is {part_one(test1)} and should be 5')
    print(f'The answer to test2 is {part_one(test2)} and should be 6')
    print(f'The answer to test3 is {part_one(test3)} and should be 10')
    print(f'The answer to test4 is {part_one(test4)} and should be 11')
    start = time.time()
    print(f"The answer to part one is {part_one(data)}")
    print(f"calculated in {time.time()-start}")
    print(f'The answer to test1 is {part_two(test1)} and should be 23')
    print(f'The answer to test2 is {part_two(test2)} and should be 23')
    print(f'The answer to test3 is {part_two(test3)} and should be 29')
    print(f'The answer to test4 is {part_two(test4)} and should be 26')
    start = time.time()
    print(f"The answer to part two is {part_two(data)}")
    print(f"calculated in {time.time()-start}")

if __name__ == "__main__":
    main()