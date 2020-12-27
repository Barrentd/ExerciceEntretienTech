
"""Function that return true or false if the select value is on even position in array"""

def is_on_even_position(table, value):

    """Verify if the select value is on even position in array

    Returns:
        bool: true or false
    """

    res_index = False

    for index, i in enumerate(table):
        if i == value:
            if index%2 == 0:
                res_index = True
    return res_index

def main():

    """Main function"""

    array_num = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ex1 = is_on_even_position(array_num, 6)
    ex2 = is_on_even_position(array_num, 3)

    print("ex1", ex1)
    print("ex2", ex2)

if __name__ == "__main__":
    main()
