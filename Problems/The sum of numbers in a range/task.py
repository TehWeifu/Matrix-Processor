def range_sum(numbers, start, end):
    total_sum = 0
    num_list = numbers.split()
    for num in num_list:
        num = int(num)
        if start <= num <= end:
            total_sum += num
    return total_sum


input_numbers = input()
a, b = input().split()
a = int(a)
b = int(b)
print(range_sum(input_numbers, a, b))
