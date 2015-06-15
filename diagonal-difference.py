def diagonal(x):
    cursor = 0
    compare = [[],[]]
    while cursor < len(x):
        compare[0].append(x[cursor][cursor])
        compare[1].append(x[cursor][-cursor - 1])
        cursor += 1
    return abs(sum(compare[0])-sum(compare[1]))

        

test_cases = int(raw_input().strip())

data = []
for _ in range(test_cases):
    data.append([int(num) for num in raw_input().strip().split()])

print diagonal(data)
