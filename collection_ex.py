def collections(name):
    # List
    ls = [1, 2, 3, 4, 5]
    print(ls)
    empty_list = []
    print(empty_list)
    print(2 in ls)
    print(7 in ls)
    print(len(ls))
    print(sorted(ls))
    print(sum(ls))

    # Accessing elements in the list.
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Getting the first element
    print(list_numbers[0])
    # Get elements from 3rd upto 4 elements
    print(list_numbers[2:4])
    # Get the last element
    print(list_numbers[-1])
    # Get last 4 elements
    print(list_numbers[-4:])
    # Get the elements from 6th to 8th
    print(list_numbers[-5:-2])

    # Adding elements to the list

    # Append - to add elements to the end of the list
    list_numbers.append(11)
    print(list_numbers)

    # Insert - To insert an element at the index specified.All the elements from that index will be moved to right side
    list_numbers.insert(3, 13)
    print(list_numbers)

    # Extend-To extend the list by appending elements from other list
    list_numbers.extend([12, 14])
    print(list_numbers)

    # Updating the elements from the list
    list_numbers[1] = 11
    print(list_numbers)

    # Removing the elements from the list

    # remove- Delete the first occurence of the element from the list
    list_numbers.remove(13)
    print(list_numbers)

    # pop-Delete the element from the list using the index
    list_numbers.pop(2)
    print(list_numbers)

    # clear-Delete all the elements from the list
    list_numbers.clear()
    print(list_numbers)

    # Other list operations
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    print(list_numbers.count(1))

    list_numbers.sort()
    print(list_numbers)

    list_numbers.reverse()
    print(list_numbers)


if __name__ == '__main__':
    collections('PyCharm')
