import threading
import os

def Task1(Value):
    print("Executing the first task...")
    print("PID of running process for task1 :",os.getpid())
    print("Thread ID of first thread :",threading.current_thread())


def Task2(Value):
    print("Executing the second task..")
    print("PID of running process for task2 :",os.getpid())
    print("Thread ID of second thread:",threading.current_thread())
    
def main():
    print("Demostration of MultiProcessing..")
    print("PID of running process is :",os.getpid())
    print("Thread ID of main thread:",threading.current_thread())

    print("__________________________________________________")
    No = 5
    t1 = threading.Thread(target = Task1, args =  (No,))
    t2 = threading.Thread(target = Task2, args = (No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print("__________________________________________________")
if __name__ =="__main__":
    main()    