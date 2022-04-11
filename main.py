import time

uptime = -1

while True:
    uptime += 1
    print("I have been awake for:")
    print(uptime, " Minutes")
    print("{:0.2f} Hours".format(uptime/60))
    print("<======================>")
    time.sleep(60)