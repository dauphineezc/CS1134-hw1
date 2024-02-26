def fibs(n):
    num_1 = 1
    num_2 = 1
    for i in range(0, n):
        if i == 0 or i == 1:
            yield 1
        else:
            curr_num = num_1 + num_2
            yield curr_num
            num_1 = num_2
            num_2 = curr_num
