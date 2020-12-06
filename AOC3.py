slope1 = (3, 1)
slopelist = [(1, 1),(3, 1),(5, 1),(7, 1),(1, 2),]

with open("inputData.txt") as f:
    trees = [line.strip() for line in f]
    width = len(trees[0])
    ans2 = 1
    for dx, dy in slopelist:
        x, y = 0, 0
        ans1 = 0

        while y < len(trees):
            if trees[y][x] == "#":
                ans1 += 1
            x = (x + dx) % width
            y += dy

        if (dx, dy) == slope1:
            print("Part 1:", ans1)

        ans2 *= ans1

    print("Part 2:", ans2)
