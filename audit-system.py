import platform
import psutil

def system_audit():
    print("=== Basic System Audit ===")
    print("OS:", platform.system(), platform.release())
    print("CPU Usage:", psutil.cpu_percent(), "%")
    print("Memory Usage:", psutil.virtual_memory().percent, "%")
    print("Disk Usage:", psutil.disk_usage('/').percent, "%")
    print("==========================")

if __name__ == "__main__":
    system_audit()
