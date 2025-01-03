# def find_max_num(array):
#     for number in array:
#         is_max_num = True
#         for compare_number in array:
#             if number < compare_number:
#                 is_max_num = False
#         if is_max_num:
#             return number
#
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
# print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))
#

# def find_max_num2(array):
#     for bigger in array:
#         is_max = True # 일단 반복문중 지금의 수가 최대값이 맞다고 가정
#         for bigger_right in  array:
#             if(bigger_right > bigger):
#                 is_max = False
#         if(is_max):
#             return bigger
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num2([3, 5, 6, 1, 2, 4]))
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num2([6, 6, 6]))
# print("정답 = 1888 / 현재 풀이 값 = ", find_max_num2([6, 9, 2, 7, 1888]))



#
# def find_max_num(array):
#     max_num = array[0]
#     print('max_num : ', max_num)
#     for num in array:
#         if num > max_num:
#             max_num = num
#     return max_num
#
#
#
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
# print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
# print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

def function_MAX_NUM(arrayNum):
    firstArray = arrayNum[0]
    for find_max_num in arrayNum:
        if(firstArray < find_max_num):
            firstArray = find_max_num
    return firstArray


print (function_MAX_NUM([1,2,3,4,5,6,10,20,40,7,2,32]))

