def parse_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()

def part1(data):
    sum = 0

    data = data[0].split(",")
    data = [list(map(int, x.split("-"))) for x in data]
    for row in data:
        for i in range(row[0], row[1] + 1):
            num = str(i)
            if len(num) % 2 != 0:
                continue
            if num[0:len(num)//2] == num[len(num)//2:]:
                sum += i
                #print(num)
    return sum
                           

def part2(data):

    invalid = set()

    data = data[0].split(",")
    data = [list(map(int, x.split("-"))) for x in data]
    for row in data:
        for i in range(row[0], row[1] + 1):
            num = str(i)
            for j in range(1,len(num)):
                if len(num)%j != 0:
                    continue
                for k in range(0, len(num), j):
                    if num[k:k+j] != num[0:j]:
                        break
                else:
                    invalid.add(i)
                    #print(num, j)
    return sum(invalid)

if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))