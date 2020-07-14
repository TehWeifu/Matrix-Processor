def average_mark(*grades):
    sum_grades = 0
    counter = 0
    for num in grades:
        sum_grades += num
        counter += 1
    return round(sum_grades / counter, 1)
