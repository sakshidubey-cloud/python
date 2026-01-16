#Normal func
# import time

# def task():
#     time.sleep(5)
#     print("5 done")
#     time.sleep(2)
#     print("2 done")

# task()    

#Multithreading
import threading
import time

def task():
    time.sleep(5)
    print("5 done")
    time.sleep(2)
    print("2 done")   

t1 = threading.Thread(target=task())
t2 = threading.Thread(target=task())

t1.start()
t2.start()

t1.join()
t2.join()