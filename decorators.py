def decorator(fun):
    def start():
        print("start")
        fun()
        print("exit")
    return start      

@decorator
def say_hi():
    print("Hi")
say_hi()