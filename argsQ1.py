def get_max(*nums):
    max = nums[0]
    for num in nums:
        if(num > max):
            max = num
    return max

print(get_max(-14, 95, -78, 33, 92, 262, 87, 55))

def get_avg(*nums):
    numslen = len(nums)
    sum = 0
    if(numslen == 0):
        print("입력받은 요소가 없습니다")
    else:
        for num in nums:
            sum += num
        avg = sum / len(nums)
        return avg
print(get_avg())