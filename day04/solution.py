def parse_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()
    
def neighbors(x, y, max_x, max_y, data):
    deltas = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]
    result = []
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < max_x and 0 <= ny < max_y:
            result.append(data[nx][ny])
    return result

def part1(data):
    sum = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == '@':
                n = neighbors(x, y, len(data), len(data[x]), data)
                if n.count('@') < 4:
                    sum += 1
    return sum

def part2(data):
    sum = 0
    positions = [(0, 0)]
    while len(positions) > 0:
        positions = []
        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y] == '@':
                    n = neighbors(x, y, len(data), len(data[x]), data)
                    if n.count('@') < 4:
                        sum += 1
                        positions.append((x, y))
        for x, y in positions:
            line = list(data[x])
            line[y] = '.'
            data[x] = "".join(line)
    return sum

if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))