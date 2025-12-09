def parse_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()

def part1(data):
    structured = []
    for item in data:
        line = item.strip().split(' ')
        line = [x for x in line if x != ""]
        structured.append(line)

    operations = []
    for i in range(len(structured[0])):
        line = []
        for j in range(len(structured)):
            line.append(structured[j][i])
        operations.append(line)

    sum = 0

    for operation in operations:
        x = int(operation[0])
        for i in range(1, len(operation)-1):
            if operation[-1] == '+':
                x += int(operation[i])
            elif operation[-1] == '*':
                x *= int(operation[i])
        sum += x

    return sum

def part2(data):
    listed = []
    for i in data:
        listed.append(list(i))
    
    columns = []
    for i in range(len(listed[0])):
        line = []
        for j in range(len(listed)):
            line.append(listed[j][i])
        columns.append(line)
    
    operations = []
    line = []
    for column in columns:
        col = ''.join(column).replace(' ', '')
        if col != '':
            if col[-1] == "+" or col[-1] == "*":
                line.append(col[-1])
                line.append(col[:-1])
            else:
                line.append(col)
        else:
            operations.append(line)
            line = []
    operations.append(line)
    
    sum = 0

    for operation in operations:
        x = int(operation[1])
        for i in range(2, len(operation)):
            if operation[0] == '+':
                x += int(operation[i])
            elif operation[0] == '*':
                x *= int(operation[i])
        sum += x
        #print(operation, x)

    return sum

if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))