# def find_max_occurred_alphabet(string):
#     alphabet_occurrence_array = [0] * 26
#
#     for char in string:
#         if not char.isalpha():
#             continue
#         alphabet_occurrence_array[ord(char) - 97] += 1
#
#     max_occurrence = 0
#
#     # for index in range(len(alphabet_occurrence_array)):
#     #     alphabet_occurrence = alphabet_occurrence_array[index]
#     #     if alphabet_occurrence > max_occurrence:
#     #         max_occurrence = alphabet_occurrence
#
#     max_occurrence = max(alphabet_occurrence_array)
#
#     max_alphabet_index = [i for i, v in enumerate(alphabet_occurrence_array) if v == max_occurrence]
#     answer = [chr(n + 97) for n in max_alphabet_index]
#     return answer
#
#
# result = find_max_occurred_alphabet
# print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
# print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

def solution(array):
    number_array = [0] * 1000
    for num in array:
        number_array[num] += 1

    max_num = max(number_array)
    max_num_index = [i for i, v in enumerate(number_array) if v == max_num]

    if len(max_num_index) > 1:
        return -1
    else:
        answer = max_num_index[0]
    return answer

result = solution
print(result([1, 2, 3, 3, 3, 4]))
print(result([1, 1, 2, 2]))
print(result([1]))