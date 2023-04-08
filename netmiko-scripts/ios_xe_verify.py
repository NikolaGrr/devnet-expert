from netmiko import ConnectHandler

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

output = conn.send_command("show ip interface brief")
print('\nshow ip interface brief________________________________________\n')
print(output)

output = conn.send_command("show vrf brief")
print('\nshow vrf brief_________________________________________________\n')
print(output)

output = conn.send_command("show ip route")
print('\nshow ip route__________________________________________________\n')
print(output)