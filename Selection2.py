def CheckEven(Value):
    if Value % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")

def main():
    print("Enter a number")
    Num = int(input())

    CheckEven(Num)


if  __name__=="__main__":
    main()