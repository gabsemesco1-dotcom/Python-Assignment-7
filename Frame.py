size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end="")
        else:
            print("_", end="")
    print()