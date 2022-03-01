"""
read the series of word and perform the binary search
"""


def binary_search(list_elements, value):
    low_bound = 0
    upper_bound = len(list_elements)-1

    while low_bound <= upper_bound:
        md = (low_bound+upper_bound)//2
        if list_elements[md] == value:
            print("the searched value:", value, "at position:", md)
            return True
        else:
            if list_elements[md] < value:
                low_bound = md+1
            else:
                upper_bound = md-1
    return False


if __name__ == '__main__':
    list_elements = []
    size = int(input("enter the size elements"))
    for i in range(1, size):
        data = (input("enter the elements:"))
        list_elements.append(data)
    print(list_elements)
    value = (input("enter the value to search"))
    if binary_search(list_elements, value):
        print("found")
    else:
        print("not found")
