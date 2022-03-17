def square_digits(num):
    x = ''
    for _ in str(num):
        x += str(int(_) ** 2)
    return int(x)


# test
num = 2345
print(square_digits(num))
