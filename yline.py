def yline(first_point, second_point, x):
    rise = second_point[1] - first_point[1]
    run = second_point[0] - first_point[0]
    m = rise/run
    b = first_point[1] - m*first_point[0]
    y = m*x + b
    print(y)
    return y

yline((1,2),(2,3),3)
