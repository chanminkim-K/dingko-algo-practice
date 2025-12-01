input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):

    all_one_count = 0
    all_zero_count = 0

    if string[0] == '0':
        all_zero_count += 1
    elif string[0] == '1':
        all_one_count += 1

    for i in range(len(string) - 1):    # i 0부터 문자열의 길이 - 2 까지
        if string[i] != string[i + 1]:
            if string[i + 1] == '1':
                all_one_count += 1
            if string[i + 1] == '0':
                all_zero_count += 1

    print(all_one_count, all_zero_count)
    return min(all_one_count, all_zero_count)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)