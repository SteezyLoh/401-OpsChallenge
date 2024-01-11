


import os
import time
import smtplib
import getpass
from email.mime.text import MIMEText

def ping_host(target_ip):
    return os.system(f"ping -c 1 {target_ip} > /dev/null 2>&1")

def send_email(sender_email, password, recipient_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

def main():
    ip_address = input("Enter the IP address: ")
    sender_email = input("Enter your email address:")
    sender_password = input("Enter your email password (Gmail app): ")
    receiver_email = input("Enter the adminstrator email:")

    previous_status = None

    try:
        with open(log_filename, "a") as log_file:
            while True:
                exit_code = ping_host(target_ip)
                current_status = "Active" if exit_code == 0 else "Inactive"
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

                if current_status != previous_status and previous_status is not None:
                    subject = f"Status Change Detected for {target_ip}"
                    body =f"{timestamp}: Host {target_ip} changed status from  {previous_status} to {current_status}"
                    send_email(sender_email, password, recipient_email, subject, body)

                print(f"{timestamp} Network {current_status} to {target_ip}")
                log_file.write(f"{timestamp} Network {current_status} to {target_ip}\n")
                log_file.flush()

                previous_status = current_status
                time.sleep(60) # Adjust the sleep time as needed

    except KeyboardInterrupt:
        print("Monitoring stopped.")            

'''
Resources:
    - https://docs.python.org/3/library/subprocess.html
    - https://www.datacamp.com/tutorial/python-subprocess
    - https://github.com/raqueltianna/ops-401/blob/main/uptimesensorpt1.py
    - https://github.com/Hector2024/ops-401-code-challenges/blob/main/uptime_sensor.py
    - https://chat.openai.com/share/55243fc9-4298-42f5-a2c6-7eae41c739ae
    - https://github.com/jmcano50/Ops401/blob/main/401Ops3.py
    - https://stackoverflow.com/questions/35750041/check-if-ping-was-successful-using-subprocess-in-python
'''