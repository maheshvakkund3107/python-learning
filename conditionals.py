def loops(name):
    i = 7
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
    # (cond)?on_true:on_false
    print("even") if i % 2 == 0 else print('odd')

    # i = int(input("Enter an integer"))
    if i == 0:
        print(f"i is 0")
    elif i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

    n = None
    print("Not None") if n else print(n)

    age = int(input("Enter age in months"))
    if age <= 6:
        print("New Born or Infant")
    elif 6 < age <= 18:
        print("Toddler")
    elif 18 < age <= 144:
        print("Grown Up")
    elif 144 < age <= 216:
        print("Youth")
    else:
        print("Adult")

    # TASK 2 : Number is divisible by 2 or 3
    n = int(input("Enter Integer:"))
    if n % 2 == 0 or n % 3 == 0:
        print(f"Number {n} is even or divisible by 3")

    # TASK 3 : Number is even and divisible by 3
    n = int(input("Enter Integer:"))
    if n % 2 == 0 and n % 3 == 0:
        print(f"Number {n} is even and divisible by 3")
    elif n % 3 == 0:
        print(f"Number {n} is divisible by 3 but not even")
    elif n % 2 == 0:
        print(f"Number {n} is even but not divisible by 3")


if __name__ == '__main__':
    loops('PyCharm')
