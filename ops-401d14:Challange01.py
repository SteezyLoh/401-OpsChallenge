import subprocess
import time
from datetime import datetime   

def ping_host(ip):
    try:
        subprocess.check_output(['ping', '-c', '1', ip], stderr=subprocess.STDOUT, text=True)
        return True
    except subprocess.CalledProcessError:
        return False
    # Send a single ICMP (ping) packet and return the code
def main():
    ip_address = '192.168.0.165' 

    while True:
 # Determins the date and time      
     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
  # lets us know if its active and ping the IP if it is
     status = "Network Active" if ping_host(ip_address) else "Network Inactive"
# Prints out the time and status and IP         
     print(f"{timestamp} {status} to {ip_address}")
# pause for 2 seconds
    time.sleep(2)

# Resources: https://stackoverflow.com/questions/35750041/check-if-ping-was-successful-using-subprocess-in-python https://chat.openai.com/share/55243fc9-4298-42f5-a2c6-7eae41c739ae

