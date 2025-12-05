from colorama import Fore, Back, Style

def parse_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()
    
def visualize(digits, first, last):
    visual = ""
    fistpos = digits.index(str(first))
    lastpos = digits[fistpos + 1:].index(str(last))
    for i in range(len(digits)):
        if i == fistpos:
            visual += Back.GREEN + digits[i] + Style.RESET_ALL
        elif i == fistpos + 1 + lastpos:
            visual += Back.RED + digits[i] + Style.RESET_ALL
        else:
            visual += digits[i]
    print(visual)

def part1(data):
    sum = 0
    for i in data:
        digits = list(map(int, i))
        first = max(digits[:-1])
        digits2 = digits[digits.index(first)+1:]
        last = max(digits2)
        sol = int(str(first) + str(last))
        sum += sol
        visualize(i, first, last)
    return sum

def visualize2(digits, start, end, positions):
    visual = ""
    for i in range(len(digits)):
        if i in positions:
            visual += Back.GREEN + digits[i] + Style.RESET_ALL
        elif i < start or i >= len(digits) + end:
            visual += Fore.LIGHTBLACK_EX + digits[i] + Style.RESET_ALL
        else:
            visual += Fore.LIGHTBLUE_EX + digits[i] + Style.RESET_ALL
    print(visual)

def part2(data):
    sum = 0
    for i in data:
        positions = []
        digits = list(map(int, i))
        sol = ""
        start = 0
        for end in range(-11,1):
            visualize2(i, start, end, positions)
            if len(digits[start:end]) == 0:
                digit = max(digits[start:])
            else:
                digit = max(digits[start:end])
            sol += str(digit)
            start = digits.index(digit, start) + 1
            positions.append(digits.index(digit, start - 1))
        visualize2(i, start, end, positions)
        print(f"Solution: {sol}")
        sum += int(sol)
            
    return sum

if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))