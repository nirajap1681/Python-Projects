def Display(*value):
    print(type(value))
    print(value)

    for i in range(len(value)):
        print(value[i])

def main():
    print("Demostration of variable number of arguements")

    Display(11,21,51)
    Display(10,20,30,40,50)

if __name__ == "__main__":
    main()
