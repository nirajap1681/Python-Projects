from functools import reduce

def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def Increase(No):
    return No + 2

def Add(A,B):
    return A + B

def main():
    Data = [5,4,9,8,13,17,12,18]
    print(Data)

    #filter()
    Output = list(filter(CheckEven,Data))
    print(Output)

    #map()
    Output1 = list(map(Increase,Output))
    print(Output1)

    #reduce()
    Output2 = reduce(Add,Output1)
    print(Output2)

if __name__ =="__main__":
    main()   