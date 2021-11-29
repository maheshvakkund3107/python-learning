import calendar


def loops(name):
    for i in range(5, 11):
        print(i)

    for j in range(1, 10, 2):
        print(j)

    a = [1, 6, 8, 3, 7, 2, 9]
    cnt = 0

    for i in a:
        if cnt % 2 == 0:
            print(i)
        cnt += 1

    for i in range(5, 15):
        if i % 2 == 0:
            print(i)

    for month in list(calendar.month_name)[1:]:
        print(month)

    salary = [100.0, 1000.0, 0.0, -100, 1200.0, None, -500]

    for sal in salary:
        if sal == None:
            print('Salary is Not Available')
        elif sal <= 0:
            print(f'Salary {sal} is invalid')

    for sal in salary:
        if not sal:
            print('Salary is Not Available')
        elif sal <= 0:
            print(f'Salary {sal} is invalid')


if __name__ == '__main__':
    loops('PyCharm')
