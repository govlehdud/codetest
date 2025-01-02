def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array: # a~z 까지 순회
        occurrence = 0      # 알파벳 갯수의 합 초기는 0으로 setting
        for char in string:     # alphabet_array와 비교할 입력값
            if char == alphabet:    # 입력값과 알파벳이 같을경우 1씩 더한다.
                occurrence += 1

        if occurrence > max_occurrence: # 값이 하나라도 있으면
            max_alphabet = alphabet
            max_occurrence = occurrence

    return max_alphabet

print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
# print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))