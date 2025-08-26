input = "abadabac"

def find_not_repeating_first_character(string):

    occurred_alphabet = find_max_occurred_alphabet(string)

    not_repeating_first_character = []
    for index in range(len(occurred_alphabet)):
        alphabet_occurred = occurred_alphabet[index]
        if alphabet_occurred == 1:
            not_repeating_first_character.append(chr(index + 97))

    for char in string:
        if char in not_repeating_first_character:
            return char

    return not_repeating_first_character

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char) - 97] += 1
    return alphabet_occurrence_array

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))