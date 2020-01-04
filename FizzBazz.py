a = 1
while a < 101:
    if a % 3 == 0:
        print("Fizz")
    if a % 5 == 0:
        print("Buzz")
    if a % 15 == 0:
        print("FizzBuzz")
    if a % 3 != 0 and a % 5 != 0 and a % 15 != 0:
        print(a)
    a += 1