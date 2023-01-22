def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def mod(n1, n2):
    return n1 % n2


def sub(n1, n2):
    return n1 - n2


print(__name__)

if __name__ == '__main__':
    import sys

    if sys.argv[1] == "addition":
        print(add(int(sys.argv[2]), int(sys.argv[3])))
    elif sys.argv[1] == "sub":
        print(sub(int(sys.argv[2]), int(sys.argv[3])))
    elif sys.argv[1] == "mul":
        print(mul(int(sys.argv[2]), int(sys.argv[3])))
    elif sys.argv[1] == "div":
        print(div(int(sys.argv[2]), int(sys.argv[3])))
    elif sys.argv[1] == "mod":
        print(mod(int(sys.argv[2]), int(sys.argv[3])))
