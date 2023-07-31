import time

while True:
    current_time = time.time()
    formatted_time = time.strftime("%H:%M:%S", time.gmtime(current_time))
    print("Current time is:", formatted_time)
    time.sleep(1)
