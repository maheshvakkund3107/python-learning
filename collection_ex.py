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

    # Set
    s = {1, 2, 3, 4}
    print(s)
    empty_set = set()
    print(empty_set)
    empty_dict = {}  # this will create a empty dict and not set
    print(empty_dict)
    print(2 in s)
    print(7 in s)
    print(len(s))
    print(sorted(s))
    print(sum(s))

    # Adding and deleting elements in Set
    set_numbers = {1, 2, 3, 3, 4, 4, 3}
    set_numbers.add(5)
    print(set_numbers)

    # update-Updates the set on which update is invoked
    # update a set with union of itself and others
    set_numbers.update({4, 5, 6, 7})
    print(set_numbers)

    # union-Returns the union of sets as a new set
    set_numbers = {1, 2, 3, 4}
    union_set = set_numbers.union({7, 8, 9, 0})
    print(union_set)

    union_set.pop()
    print(union_set)

    # remove-Removes an element from a set.
    # Throws error if element does not exist
    union_set.remove(2)
    print(union_set)

    # discard -Removes an element from set.
    # No error if the element does not exist
    union_set.discard(14)
    print(union_set)

    union_set.clear()
    print(union_set)

    # Typical Set Operations
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6, 7}

    print(s1.union(s2))
    print(s1.intersection(s2))
    print(s1.difference(s2))
    # Validation of set is missing here


if __name__ == '__main__':
    collections('PyCharm')
