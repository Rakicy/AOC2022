'''
Second try with a different approach
'''
def get_input_try_two(file_name):
    with open(file_name, 'r') as f:
        data = [line.split() for line in f.read().splitlines()]
    return data

def part_one_try_two(data):
    tally = 0
    my_hands = {'X':0, 'Y':1, 'Z':2}
    op_hands = {'A':0, 'B':1, 'C':2}
    '''
          X  Y  Z
          -------
      A | 3  6  0
      B | 0  3  6
      C | 6  0  3
    '''
    compare = [[3, 6, 0],
               [0, 3, 6],
               [6, 0, 3]
            ]
    for rnd in data:
        my_hand = rnd[1]
        op_hand = rnd[0]
        tally += my_hands[my_hand] + 1
        tally += compare[op_hands[op_hand]][my_hands[my_hand]]
    return tally

def part_two_try_two(data):
    tally = 0
    lose_draw_win = {'X':0, 'Y':1, 'Z':2}
    op_hands = {'A':0, 'B':1, 'C':2}
    '''
          X  Y  Z
          -------
      A | 3  1  2
      B | 1  2  3
      C | 2  3  1
    '''
    compare = [[3, 1, 2],
               [1, 2, 3],
               [2, 3, 1]
            ]
    for rnd in data:
        outcome = rnd[1]
        op_hand = rnd[0]
        tally += lose_draw_win[outcome] * 3
        tally += compare[lose_draw_win[outcome]][op_hands[op_hand]]
    return tally

def main():
    file_name = r"Advent of Code\2022\day02.txt"
    # Second try
    data = get_input_try_two(file_name)
    print(f"The answer to part one is {part_one_try_two(data)}")
    print(f"The answer to part two is {part_two_try_two(data)}")


if __name__ == "__main__":
    main()