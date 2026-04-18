size = 5
for i in range(size):
    for j in range(size):
        if i == 2 or j == 2:
            print("*", end="")
        else:
            print("_", end="")
    print()