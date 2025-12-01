def calculate_zeros_hit(filename):

    pos = 50
    x = 0

    with open(filename, "r") as f:
        lines = f.readlines()

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


def calculate_crossings(filename):

    pos = 50
    x = 0
    last_pos = 50
    
    with open(filename, "r") as f:
        lines = f.readlines()

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

print(calculate_zeros_hit("1/1.txt"))
print(calculate_crossings("1/1.txt"))