class Number:
    """
    in this we are going to Guessing the number which is given input we perform the power of two then perform the
    binary search for the guessing number
    """
    def guess_number(value):
        n = value
        low_bound = 1
        upper_bound = 2 ** n
        print("low:", low_bound, "upper:", upper_bound)

        while low_bound <= upper_bound:
            md = (low_bound+upper_bound)//2
            print("mid value:", md)
            if md == value:
                print("the searched value:", value, "at position:", md)
                return True
            else:
                if md < value:
                    low_bound = md+1
                    print("lowfinding:", low_bound)
                else:
                    upper_bound = md-1
                    print("upperfinding:", upper_bound)
        return False


if __name__ == '__main__':
    number = int(input("enter the value for guess"))
    if Number.guess_number(number):
        print("found", number)
