# 시간 복잡도
def find_max_num(array):

    # 첫번쨰 풀이방법

    # for number in array:
    #     is_max_num = True
    #     for compare_number in array:
    #         if number < compare_number:
    #             is_max_num = False
    #     if is_max_num:
    #         return number

    # 두번쨰 풀이방법
    max_array_num = array[0]
    for array_num in array:
        if max_array_num < array_num:
            max_array_num = array_num
    return max_array_num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))

# 둘다 정답이 도출 되지만  연산량이 차이가 난다
# 첫번쨰는 2N * 2 + N 이고 두번쨰는 2N + 1이다
# 비교하기쉽게 빅오계산법으로 보면 N² 와 N의 차이이다
# 제곱의 차이니까 N의 값이 늘어날수록 연산량도 확연히 차이가 날것이다.