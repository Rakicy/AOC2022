def get_input(file_name):
    with open(file_name, 'r') as f:
        data = f.read().splitlines()
    return data

def part_one(data):
    '''
    A, X = Rock 1 point
    B, Y = Paper 2 points
    C, Z = Scissors 3 points
    win = 6 points
    lose = 0 points
    draw = 3 points
    '''
    guide = {'A X':1 + 3, 'A Y':2 + 6, 'A Z':3 + 0,
             'B X':1 + 0, 'B Y':2 + 3, 'B Z':3 + 6,
             'C X':1 + 6, 'C Y':2 + 0, 'C Z':3 + 3
             }
    return sum([guide[rnd] for rnd in data])

def part_two(data):
    '''
    A = Rock 1 point
    B = Paper 2 points
    C = Scissors 3 points
    X (lose) = 0 points
    Y (draw) = 3 points
    Z (win) = 6 points
    '''
    guide = {'A X':3 + 0, 'A Y':1 + 3, 'A Z':2 + 6,
             'B X':1 + 0, 'B Y':2 + 3, 'B Z':3 + 6,
             'C X':2 + 0, 'C Y':3 + 3, 'C Z':1 + 6
             }
    return sum([guide[rnd] for rnd in data])

def main():
    file_name = r"Advent of Code\2022\day02.txt"
    data = get_input(file_name)
    print(f"The answer to part one is {part_one(data)}")
    print(f"The answer to part two is {part_two(data)}")

if __name__ == "__main__":
    main()