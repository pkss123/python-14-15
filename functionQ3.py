def calc_rangesum(start, end):
    sum = 0
    for num in range(start, end + 1):
        sum += num
    return sum

result = calc_rangesum(4, 6)
print("4부터 6까지의 누적합계 : ",result)

result = calc_rangesum(6, 9)
print("6부터 9까지의 누적합계 : ",result)