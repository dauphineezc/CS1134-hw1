def shift(lst, k, direction="left"):
    counter = 0
    while counter < k:
        if direction == "left":
            num = lst.pop(0)
            lst.append(num)
        elif direction == "right":
            num = lst.pop(len(lst)-1)
            lst.insert(0, num)
        counter += 1

    return lst
