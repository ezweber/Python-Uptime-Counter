import psutil
import os

uptime = -1

while True:
    cpu_usage = psutil.cpu_percent(2)
    uptime += 1
    print("I have been awake for:")
    print(uptime, " Minutes")
    print("{:0.2f} Hours".format(uptime/60))
    print("Average CPU usage for last 60 seconds: ", cpu_usage)
    print("RAM usage: ", psutil.virtual_memory()[2])
    print("<======================>")
