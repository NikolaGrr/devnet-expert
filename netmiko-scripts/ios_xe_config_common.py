from netmiko import ConnectHandler

# Define device connection info
cisco_xe_csr8000v = {
    'device_type' : 'cisco_xe',
    'ip' : 'sandbox-iosxe-latest-1.cisco.com',
    'username' : 'admin',
    'password' : 'C1sco12345'
}

# Define configuration commands as a list
common_config = [
    'interface GigabitEthernet 3',
    'description Network Interface'
]

# Start a connection
net_connect = ConnectHandler(**cisco_xe_csr8000v)
print(net_connect.find_prompt())
# Send configuration commands to device
output = net_connect.send_config_set(common_config)
print(output)   # Display device response to each command

output = net_connect.send_command('show ip int brief')
print(output)