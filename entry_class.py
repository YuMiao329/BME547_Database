def tryme():
    try:
        from teeto import sqrt
    except:
        from math import sqrt

    x = sqrt(4)
    print(x)


def main():
    tryme()
    from my_cal import add_posinteger
    try:
        x = add_posinteger(-1, 2)
        print(x)
    except ValueError as err:
        print(err)
    except:
        print("all other errors")


if __name__ == "__main__":
    main()
