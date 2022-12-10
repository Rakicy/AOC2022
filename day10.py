import time
import re
def get_input(file_name):
    with open(file_name, 'r') as f:
        data = f.read().splitlines()
    return data

def part_one(data):
    num_stream = get_num_stream(data)
    return get_signals(num_stream)

def get_signals(num_stream):
    total_signal = 0
    for signal in range(19,len(num_stream),40):
        total_signal += (signal+1)*num_stream[signal]
    return total_signal

def get_num_stream(data):
    data_stream_x = []
    num_x = 1
    for instruction in data:
        if not(instruction.find('noop') == -1):
            data_stream_x.append(num_x)
        else:
            data_stream_x.append(num_x)
            data_stream_x.append(num_x)
            num = int(re.findall('(-?\d+)', instruction)[0])
            num_x += num
    return data_stream_x


def part_two(data):
    num_stream = get_num_stream(data)
    display = get_hash_locations(num_stream)
    print_screen(display)
    return "'Check above in the output screen'"

def get_hash_locations(num_stream):
    crt_screen = ['.' for _ in range(240)]
    screen_width = 40
    for location,number in enumerate(num_stream):
        column = location % screen_width
        window_to_search = [column-1,column,column+1]
        if number in window_to_search:
            crt_screen[location] = '#'
    return crt_screen


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def print_screen(crt_screen):
    screen_width = 40
    for line in chunker(crt_screen,screen_width):
        print(' '.join(line))
    print()

def main():
    file_name = r"Advent of Code\2022\day10.txt"
    data = get_input(file_name)
    start = time.time()
    print(f"The answer to part one is {part_one(data)}")
    print(f"calculated in {time.time()-start}")
    start = time.time()
    print(f"The answer to part two is {part_two(data)}")
    print(f"calculated in {time.time()-start}")

if __name__ == "__main__":
    main()