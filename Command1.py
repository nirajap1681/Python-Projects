import sys

def main():
    print("Demostration of Command line Arguements")

    print("Number of command line arguements are:",len(sys.argv))

    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
if __name__ == "__main__":
    main()

#py Command1.py marvellous 11
