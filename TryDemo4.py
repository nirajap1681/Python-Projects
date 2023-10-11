def main():
    try :
        print("Enter First Number:")
        No1 = int(input())

        print("Enter Second Number:")
        No2 = int(input())

        Ans = 0

        Ans = No1/No2

    except ZeroDivisionError as zobj:
        print("ZeroDivision Exception Occured as ==> ",zobj)
        return

    except ValueError as vobj:
        print("ValueError Exception Occured as ==> ",vobj)
        return

    except Exception as eobj:
        print("Exception Occured as ==> ",eobj)
        return

    finally :
        print("Thank You!!!!!")

    print("Division is : ",Ans)


if __name__ == "__main__":
    main()