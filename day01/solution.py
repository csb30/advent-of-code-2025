def parse_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()

def part1(data):
    pos = 50
    x = 0

    lines = data

    for i in lines:
        dir = i[0]
        val = int(i[1:])
        if dir == "L":
            pos -= val
        elif dir == "R":
            pos += val
        pos = pos % 100
        if pos == 0:
            x += 1

    return x

def part2(data):
    pos = 50
    x = 0
    last_pos = 50
    
    lines = data

    for i in lines:
        add = 0
        last_pos = pos
        dir = i[0]
        val = int(i[1:])
        if dir == "L":
            pos -= val
        elif dir == "R":
            pos += val
        
        if pos <= 0:
            add = (-pos // 100) + 1
            if last_pos == 0 and add > 0:
                add -= 1
        elif pos >= 100:
            add = ((pos-100) // 100) + 1
        x += add
        pos = pos % 100

    return x

if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))