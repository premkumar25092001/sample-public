import time 
def task(taskName,delay):
    print(f"Task {taskName} started")
    time.sleep(delay)
    print(f"Task {taskName} completed")

startTime = time.time()
task("1",2)
task("2",1)
task("3",3)
endTime = time.time()
print(f"Time taken: {endTime-startTime:2f}")