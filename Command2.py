import sys

def main():
    print("Demostration of Command line Arguements")

    Value1 = int(sys.argv[1])
    Value2 = int(sys.argv[2])
    Ans = Value1 +Value2

    print("Addition is :",Ans)

if __name__ == "__main__":
    main()


