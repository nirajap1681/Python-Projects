def DisplayFactors(Num):
    print("---------------------")
    No =1
    while(No<Num):
        if Num % No == 0:
            print(No)
        No = No +1    
    print("---------------------")

def main():
    print("Enter the number")
    Num = int(input())
    DisplayFactors(Num)

if __name__ == "__main__":
    main()