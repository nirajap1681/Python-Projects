import sys
i = 1

def Display():
    global i
    print("Inside Display",i)
    i+=1
    Display()
    
def main():
    print("Recursion limit is : ",sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    Display()

if __name__ == "__main__":
    main()