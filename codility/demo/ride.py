def smallest():
    arr = [1, 3, 6, 4, 1, 2]
    max = 1
    temp = sorted(arr)
    for tmp in temp:
        if tmp == max:
            max += 1
    print(max)

if __name__ == "__main__":
    smallest()