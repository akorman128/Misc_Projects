#Project Euler 16

# def power_sum(exp):
#     sum = 0
#
#     power = 2**exp
#     power = str(power)
#     for x in range(len(power)):
#         sum += int(power[x])
#     return sum
#
# power_sum(1000)

#_______________________

# def fibonacci_sum(num):
#     fib = [1,2]
#     sum = 2
#     for x in range(num):
#         next = fib[len(fib)-1] + fib[len(fib)-2]
#         fib.append(next)
#         if next % 2 == 0:
#             sum += next
#     print(sum)
#     return sum
#
# fibonacci_sum(4000000)


#project euler 1

# def multiple_three_five(num):
#     list = 0
#     for x in range(num):
#         if x % 3 == 0 or x % 5 == 0:
#             list += x
#     print(list)
#     return list
#
# multiple_three_five(1000)
