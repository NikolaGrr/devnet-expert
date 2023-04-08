from netmiko import ConnectHandler
import json

# Define device connection information
cisco_xe_csr8000v = {
    'device_type' : 'cisco_xe',
    'ip' : 'sandbox-iosxe-latest-1.cisco.com',
    'username' : 'admin',
    'password' : 'C1sco12345'
}

# Start a device connection
conn = ConnectHandler(**cisco_xe_csr8000v)

# Find exec mode prompt
conn.find_prompt()

output = conn.send_command("show ip interface brief", use_textfsm=True)
print('\nshow ip interface brief________________________________________\n')
print(json.dumps(output, indent=2))

output = conn.send_command("show vrf brief", use_textfsm=True)
print('\nshow vrf brief_________________________________________________\n')
print(json.dumps(output, indent=2))

output = conn.send_command("show ip route", use_textfsm=True)
print('\nshow ip route__________________________________________________\n')
print(json.dumps(output, indent=2))