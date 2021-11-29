import calendar
import datetime as dt
import math
from operator import add, mul, truediv, sub, mod


def predefined_functions():
    # Numeric Functions
    print(add(4, 5))
    print(mul(4, 5))
    print(truediv(4, 5))
    print(sub(5, 4))
    print(mod(5, 4))
    print(pow(2, 3))
    print(math.pow(2, 3))
    print(math.ceil(3.4))
    print(math.floor(3.7))
    print(round(3.7))
    print(math.sqrt(4))
    print(min(4, 3, 1, 8, 9, 2, 10))
    print(max(4, 3, 1, 8, 9, 2, 10))

    # String Functions
    s = "Hello World"
    print(s[:5])
    print(s[-5:])
    print(len(s))
    print(sorted(s))

    user = '1,123 456 789,Scott,Tiger,1989-08-15,+1 415 891 9002,Forrest City,Texas,75063'
    first_name = user.split(',')[2]
    print(first_name)
    print(first_name.upper())

    last_name = user.split(',')[3]
    print(last_name)
    print(last_name.lower())

    full_name = (first_name + ' ' + last_name).capitalize()
    print(full_name)

    dob = user.split(',')[4]
    print(dob)
    print(int(dob[0:4]))
    d = dt.datetime.strptime(user.split(',')[4], "%Y-%m-%d")
    print(d)

    print("Current date with timestamp")
    print(dt.datetime.now())
    print("Current date without timestamp")
    print(dt.date.today())

    print("Converting date to string in the form of yyyy-MM-dd")
    print(dt.datetime.today().strftime("%Y-%m-%d"))
    print("Converting date to string in the form of dd-MM-yyyy")
    print(dt.datetime.today().strftime("%d-%m-%Y"))
    print("Converting date to string in the form of yyyy/MM/dd")
    print(dt.datetime.today().strftime("%Y/%m/%d"))
    print("Converting date to string in the form of yyyyMMdd")
    print(dt.datetime.today().strftime("%Y%m%d"))
    print("Converting date to integer in the form of yyyyMMdd")
    print(int(dt.datetime.today().strftime("%Y%m%d")))
    # Converting string which contains date using format yyyy-MM-dd as date
    print(dt.datetime.strptime('2020-10-07', '%Y-%m-%d'))
    print(dt.datetime.strptime('2020-10-07', '%Y-%m-%d').date())
    # Converting number which contains date using format yyyyMMdd as date
    # strptime expects first argument to be string which contain date
    # so we need to convert datatype of number to string
    print(dt.datetime.strptime(str(20201007), '%Y%m%d'))
    # Converting string which contains timestamp using format yyyy-MM-dd HH:mm:ss as date
    print(dt.datetime.strptime('2020-10-07 21:09:10', '%Y-%m-%d %H:%M:%S'))
    d = dt.date.today()
    print(d)
    print(calendar.weekday(d.year, d.month, d.day))
    print(calendar.day_name[calendar.weekday(d.year, d.month, d.day)])


if __name__ == '__main__':
    predefined_functions()
