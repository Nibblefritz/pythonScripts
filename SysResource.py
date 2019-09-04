import psutil

print("CPU")

#get cpu times
print(psutil.cpu_times())

#get cpu percentage every 1 second for cpus in general
for x in range(3):
    print(psutil.cpu_times_percent(interval=1, percpu=False))

#get amount of cpus
print(psutil.cpu_count())

#get cpu statistics
print(psutil.cpu_stats())

#get cpu freq
print(psutil.cpu_freq())

#get load average
print(psutil.getloadavg())

print("Memory")

#virtual
print(psutil.virtual_memory())

#swap
print(psutil.swap_memory())

#get in gigabyte blocks
print("Total RAM: ", end = ''), print(round(psutil.virtual_memory().total / (1024.0 ** 3), 2), end = ''), print(" GB")
print("Available RAM: ", end = ''), print(round(psutil.virtual_memory().available / (1024.0 ** 3), 2), end = ''), print(" GB")
print("Percent in use: ", end = ''), print(psutil.virtual_memory().percent, end = ''), print("%")
print("RAM in use: ", end = ''), print(round(psutil.virtual_memory().used / (1024.0 ** 3), 2), end = ''), print(" GB")
print("RAM free: ", end = ''), print(round(psutil.virtual_memory().free / (1024.0 ** 3), 2), end = ''), print(" GB")

print("Total SWAP: ", end = ''), print(round(psutil.swap_memory().total / (1024 ** 3), 2), end = ''), print(" GB")
print("SWAP used: ", end = ''), print(round(psutil.swap_memory().used / (1024 ** 3), 2), end = ''), print(" GB")
print("SWAP free: ", end = ''), print(round(psutil.swap_memory().free / (1024 ** 3), 2), end = ''), print(" GB")
print("SWAP Percent used: ", end = ''), print(psutil.swap_memory().percent, end = ''), print("%")

print("Disks")

print(psutil.disk_partitions())
print(psutil.disk_usage('C:\\'))
print(psutil.disk_io_counters('C:\\'))
