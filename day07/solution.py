def parse_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()

def part1(data):
    lines = [list(line) for line in data if line.strip() != '']
    
    beams = set()
    beams.add(lines[0].index("S"))

    c = 0

    for row in range(1, len(lines)):
        ind = [i for i, val in enumerate(lines[row]) if val == "^"]
        for i in ind:
            if i in beams:
                beams.remove(i)
                beams.add(i - 1)
                beams.add(i + 1)
                c += 1
        for i in beams:
            lines[row][i] = "|"
        print("".join(lines[row]))

    return c
    

def part2(data):
    lines = [list(line) for line in data if line.strip() != '']

    beam = lines[0].index("S")
    cache = {}
    return calcpath(lines[1:], beam, cache, 0)

def calcpath(lines, beam, cache, depth):
    print(f"calcpath called with beam={beam}, depth={depth}, lines left={len(lines)}")
    if (beam, depth) in cache:
        print(f"Using cached value for beam={beam}, depth={depth}")
        return cache[(beam, depth)]
    if len(lines) == 0:
        return 1
    ind = [i for i, val in enumerate(lines[0]) if val == "^"]
    if beam in ind:
        ret = calcpath(lines[1:], beam - 1, cache, depth + 1) + calcpath(lines[1:], beam + 1, cache, depth + 1)
        if ret > 5:
            cache[(beam, depth)] = ret
        return ret
    else:
        ret = calcpath(lines[1:], beam, cache, depth + 1)
        if ret > 5:
            cache[(beam, depth)] = ret
        return ret
            

if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))