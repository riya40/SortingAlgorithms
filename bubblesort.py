"""
Sort the list of number by the given input using the bubble sort
"""


def bubble_sort(array):
    for i in range(0, len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    print(array)


if __name__ == '__main__':
    list_elements = []
    size = int(input("enter the size elements"))
    for i in range(1, size):
        data = (input("enter the elements:"))
        list_elements.append(data)
    print(list_elements)
    print('insertion sort ordered elements:')
    bubble_sort(list_elements)
