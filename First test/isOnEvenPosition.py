
t = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def is_on_even_position(table, value):
    for index, i in enumerate(table):

        if (i == value):
            if(index%2 == 0):
                return True
            else:
                return False

def main():
    t = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ex1 = is_on_even_position(t, 6)
    ex2 = is_on_even_position(t, 3)

    print("ex1", ex1)
    print("ex2", ex2)

if __name__ == "__main__":
    main()