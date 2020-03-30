nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []

# List
# ===============

#  want 'n*n' for each 'n' n nums
# for n in nums:
#     my_list.append(n*n)
# or
# my_list = [n for n in nums]
# my_list = [n*n for n in nums]
# my_list = map(lambda n: n*n, nums)

# want 'n' for each 'n' in nums if 'n' is even
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)
# or
# my_list = [n for n in nums if n % 2 == 0]
# using filter + lambda
# my_list = filter(lambda n: n % 2 == 0, nums)

# want a (letter, num) pair for each letter 'abcd' and each number in '0123'
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# or
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# Dictionary
#  =====================

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# want a dict{'name':'hero'} for each name, hero in zip(names, heros)

# print(list(zip(names, heros)))
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)
# or
# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)

# dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
# print(list(map(lambda x: x['name'], dict_a)))  # Output: ['python', 'java']


# Set
# ================
# nums = [0, 0, 5, 2, 4, 7, 8, 9, 5, 6, 4, 6, 2, 1, 0, 2, 0, 1]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# or
# my_set = {n for n in nums}
# print(my_set)

#  Generator expressions
# ===========================

def gen_func(nums):
    for n in nums:
        yield n*n


# my_gen = gen_func(nums)

# for i in my_gen:
#     print(i)

my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)
