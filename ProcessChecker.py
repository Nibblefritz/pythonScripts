import psutil, os, time

print(psutil.pids())

entry = input("Enter the PID you want info on: ")
p = psutil.Process(int(entry))

print()
print("INFO")
print("Process PID: ", end = ''), print(p.pid)
print("Process Name: ", end = ''), print(p.name())
print("Process Executable: ", end = ''), print (p.exe())
print("Process CWD: ", end = ''), print(p.cwd())
print("Process command line: ", end = ''), print(p.cmdline())
print("Status: ", end = ''), print(p.status())
print("User Running Process: ", end = ''), print(p.username())
print("Running Since: ", end = ''), print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.create_time())))
print()
print("UTILIZATION")
print("CPU Usage: ", end = ''), print(p.cpu_percent())
print("Memory Usage: ", end = ''), print(p.memory_percent())
print()
print("I/O")
print(p.io_counters())
print()
print("Open Files:")
print(p.open_files())
print()
print("Network Connections:")
print(p.connections())



print()
print("Process PPID: ", end =''), print(p.ppid())
pp = psutil.Process(p.ppid())
print("PPID Process Name: ", end =''), print(pp.name())

print()
print(p.children(recursive=True))

