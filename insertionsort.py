"""
Reads the list of Strings given by user
Shows the Sorted Manner using the Insertion sort
"""


def insertion_sort(elements):
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0:
            if key < elements[j]:
                elements[j + 1] = elements[j]
                elements[j] = key
                j = j - 1
            else:
                break
    print(elements)


if __name__ == '__main__':
    list_elements = []
    size = int(input("enter the size elements"))
    for i in range(1, size):
        data = (input("enter the elements:"))
        list_elements.append(data)
    print(list_elements)
    print('insertion sort ordered elements:')
    insertion_sort(list_elements)
