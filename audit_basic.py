import platform
import psutil
import socket
import subprocess
import os

def basic_system_info():
    print("\n=== Basic System Information ===")
    print("OS:", platform.system(), platform.release())
    print("Hostname:", socket.gethostname())
    print("Architecture:", platform.machine())
    print("CPU Usage:", psutil.cpu_percent(), "%")
    print("Memory Usage:", psutil.virtual_memory().percent, "%")
    print("Disk Usage:", psutil.disk_usage('/').percent, "%")

def running_processes():
    print("\n=== Top Running Processes (by memory) ===")
    processes = [(p.info['name'], p.info['memory_percent']) 
                 for p in psutil.process_iter(['name', 'memory_percent'])]
    top = sorted(processes, key=lambda x: x[1], reverse=True)[:5]
    for name, mem in top:
        print(f"{name:<25} {mem:.2f}% memory")

def network_connections():
    print("\n=== Open Network Connections ===")
    conns = psutil.net_connections(kind='inet')
    for c in conns[:10]:  # just show first 10
        laddr = f"{c.laddr.ip}:{c.laddr.port}" if c.laddr else ""
        raddr = f"{c.raddr.ip}:{c.raddr.port}" if c.raddr else ""
        print(f"{c.pid:<6} {c.status:<12} {laddr:<22} -> {raddr}")

def firewall_status():
    print("\n=== Windows Firewall Status ===")
    try:
        output = subprocess.check_output(
            ["netsh", "advfirewall", "show", "allprofiles"],
            shell=True,
            text=True,
            stderr=subprocess.STDOUT
        )
        print(output)
    except Exception as e:
        print("Could not check firewall status:", e)

def audit():
    basic_system_info()
    running_processes()
    network_connections()
    firewall_status()

if __name__ == "__main__":
    audit()
