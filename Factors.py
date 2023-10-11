def DisplayFactors(Num):
    print("---------------------")

    for No in range(1,Num+1):
        if Num % No == 0:
            print(No)
    print("---------------------")

def main():
    print("Enter the number")
    Num = int(input())
    DisplayFactors(Num)

if __name__ == "__main__":
    main()