import platform
import os

print("System Audit Script")
print("OS:" platform.system(),platform.release())
print("User:", os.getlogin())