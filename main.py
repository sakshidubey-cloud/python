#Normal func
# import time

# def func():
#     time.sleep(5)
#     print("5 sec")
#     time.sleep(2)
#     print("2 sec")

# func()

#AsyncIO
import asyncio

async def task():
    await asyncio.sleep(5)
    print("Done")

async def main():
    await asyncio.gather(task(), task()) 
    task.join()

asyncio.run(main())    
    