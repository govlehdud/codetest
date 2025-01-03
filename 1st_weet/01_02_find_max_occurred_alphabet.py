# def find_max_occurred_alphabet(string):
#     alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
#                       "t", "u", "v", "x", "y", "z"]
#     max_occurrence = 0 # 최대값 0으로 시작
#     max_alphabet = alphabet_array[0] # 배열 첫번쨰 값부터 순회 시작
#
#     for alphabet in alphabet_array: # a~z 까지 순회
#         occurrence = 0      # 알파벳 갯수의 합 초기는 0으로 setting
#         for char in string:     # alphabet_array와 비교할 입력값
#             if char == alphabet:    # 입력값과 알파벳이 같을경우 1씩 더한다.
#                 occurrence += 1
#
#         if occurrence > max_occurrence: # 최대값보다 현재 순회한 알파뱃 순자를 넘었을경우
#             max_alphabet = alphabet # 최대값을 가지고있는 알파벳 갱신
#             max_occurrence = occurrence # 최대값 갱신
#
#     return max_alphabet # 최대값을 가지고있는 알파벳
#
# print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
# print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))


def Function_FIND_MAX_STRING(input_string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    max_value = 0
    max_alphabet = alphabet_array[0]
    for alphabet in alphabet_array:
        num_value = 0
        for compare_num1 in input_string:
            if compare_num1 == max_alphabet:
                num_value += 1
        if num_value > max_value:
            max_value       = num_value
            max_alphabet    = alphabet
    print('1 : ' ,max_value)
    print('2 : ' ,max_alphabet)

Function_FIND_MAX_STRING('hello my name is KDY haha awsome name')