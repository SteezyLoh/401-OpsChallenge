#!/usr/bin/env python3

# Script Name:                          port_scanner.py 
# Author name:                          Scotty Jokon
# Date of latest revision:              3/6/2024
# Purpose:                              to determine if a target port is open or closed,
# Execution:                            python3 
# Additional Resources:                 https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-44/challenges/DEMO.md, https://docs.python.org/3/library/socket.html, https://chat.openai.com/share/195abccf-2fa3-4476-ac87-66f03fcebaac, https://github.com/israelqui/Ops-401-Challenges/blob/main/challenge42.py

import nmap
import ipaddress

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

# Validate IP address format
try:
    ip_address = ipaddress.ip_address(ip_addr)
except ValueError:
    print("Invalid IP address format.")
    exit()

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Full TCP Connect Scan\n""")

print("You have selected option: ", resp)

port_range = input("Enter port range (e.g., 1-100): ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sT')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
else:
    print("Please enter a valid option.")