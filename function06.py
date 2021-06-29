# return구문의 용도는 사실 두 가지 입니다
# 1. return 값을 호출한 위치에 가져다 둔다
# 2. return문 실행시 즉시 함수를 종료한다
# 이 두 가지는 동시에 진행되는 로직입니다
# 따라서 문장에 2개 이상의 return문을 작성하면 첫 번째 리턴문 까지만
# 함수가 실행되고 바로 종료됩니다

def sum_and_sub(n1,n2):
    return n1 + n2
    return n1 - n2

result = sum_and_sub(3, 7)
print(result)