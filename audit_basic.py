import platform
import os
import psutil # extra library for system details

def basic_audit():
   print("=== Basic System Audit ===")
   print(f"Operating System: {platform.system()} {platform.release()}")
   print(f"Architecture: {platform.machine()}")
   print(f"Python Version: {platform.python_version()}")
   print(f"Current User: {os.getlogin()}")
   print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
   print(f"Memory (Total): {round(psutil.virtual_memory().total / (1024**3), 2)} GB")

   print("\nTop 5 processes by memory usage:")
   for proc in sorted(psutil.process_iter(['pid', 'name', 'memory_info']),
                      key=lambda p: p.info['memory_info'].rss, reverse=True)[:5]:
        print(f"PID {proc.info['pid']:>5} | {proc.info['name']:<25} | {proc.info['memory_info'].rss / (1024**2):.2f} MB")
if __name__ == "__main__":
   basic_audit()
