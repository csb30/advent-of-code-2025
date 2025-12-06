from tqdm import tqdm

def parse_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()

def part1(data):
    fresh = []
    sum = 0
    empty = False
    for line in tqdm(data, desc="Processing lines"):
        if line == "":
            empty = True
            continue

        if not empty:
            r = line.split("-")
            fresh.append(range(int(r[0]), int(r[1]) + 1))
        else:
            for i in fresh:
                if int(line) in i:
                    sum += 1
                    break
    return sum

def part2(data):
    fresh = []
    sum = 0
    for line in tqdm(data, desc="Processing lines"):
        if line == "":
            break
        r = line.split("-")
        fresh.append([int(r[0]), int(r[1])])

    n = len(fresh)

    fresh.sort()

    print("Sorted intervals:", fresh)
    res = []

    # Checking for all possible overlaps
    for i in range(n):
        start = fresh[i][0]
        end = fresh[i][1]

        # Skipping already merged intervals
        if res and res[-1][1] >= end:
            continue

        # Find the end of the merged range
        for j in range(i + 1, n):
            if fresh[j][0] <= end:
                end = max(end, fresh[j][1])
        res.append([start, end])

    print("Merged intervals:", res)

    for i in res:
        interval_length = i[1] - i[0] + 1
        sum += interval_length

    return sum

if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))