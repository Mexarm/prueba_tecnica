from script import get_greatest


def main():
    argslst = [('283910', 2), ('1234567890', 5)]
    for args in argslst:
        print("get_gratest('%s',%s) => %d" % (*args, get_greatest(*args)))


if __name__ == "__main__":
    main()
