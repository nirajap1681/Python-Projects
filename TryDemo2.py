
def main():
    print("Enter First Number:")
    No1 = int(input())

    print("Enter Second Number:")
    No2 = int(input())

    Ans = 0
    
    try :
        Ans = No1/No2

    except ZeroDivisionError as zobj :
        print("You Cannot Divide a number by Zero =>",zobj)
        return

    print("Division is : ",Ans)

if __name__ == "__main__":
    main()