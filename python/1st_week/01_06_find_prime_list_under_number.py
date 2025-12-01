## 1
# input = 20
#
# def find_prime_list_under_number(number):
#     prime_list = []
#     for num in range(2, number+1):
#         if num == 2:
#             prime_list.append(num)
#             continue
#         for check_num in range(2, num+1):
#             if num % check_num == 0:
#                 if check_num != num and check_num >= 2:
#                     break
#                 prime_list.append(num)
#
#     return prime_list
#
#
# result = find_prime_list_under_number(input)
# print(result)

## 2. 개선
# input = 20
#
# def find_prime_list_under_number(number):
#     prime_list = []
#     for num in range(2, number+1):
#         for check_num in range(2, num):
#             if num % check_num == 0:
#                 break
#         else:
#             prime_list.append(num)
#
#     return prime_list
#
#
# result = find_prime_list_under_number(input)
# print(result)

## 3. 개선
### -> 2부터 n-1 까지 모든 수 로 나누어 떨어지지 않는지 확인하는 것이 아니라, 2부터 n-1 까지 모든 소수 로 나누어 떨어지지 않는지 알아보도록 개선
### -> 바로 직전에 찾은 소수를 이용
# input = 20
#
# def find_prime_list_under_number(number):
#     prime_list = []
#     for num in range(2, number+1):
#
#         for check_num in prime_list:
#             if num % check_num == 0:
#                 break
#         else:
#             prime_list.append(num)
#
#     return prime_list
#
#
# result = find_prime_list_under_number(input)
# print(result)

## 4. 개선
### -> 주어진 자연수 N이 소수이기 위한 필요충분 조건은 N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
###    수가 수를 나누면 몫이 발생하게 되는데 몫과 나누는 수, 둘 중 하나는 반드시 N의 제곱근 이하이기 때문
###    이를 이용해서 i * i ≤ n 일 때까지만 비교

input = 20

def find_prime_list_under_number(number):
    prime_list = []
    for num in range(2, number+1):

        for i in prime_list:
            if i * i <= num and num % i == 0:
                break
        else:
            prime_list.append(num)

    return prime_list


result = find_prime_list_under_number(input)
print(result)