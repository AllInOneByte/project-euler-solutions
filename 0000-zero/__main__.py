squares = (i ** 2 for i in range(1, 990_001))
odd_squares = filter(lambda x: x % 2 != 0, squares)
print(sum(odd_squares))