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

# Send interface configuration commands from file
output = conn.send_config_from_file('netmiko-scripts/device_cfg_files/cisco_xe_intf.cfg')
# Display device response to each command
print(output)

# Send vrf configuration commands from file
output = conn.send_config_from_file('netmiko-scripts/device_cfg_files/cisco_xe_vrf.cfg')
# Display device response to each command
print(output)

# # Apply configuration changes
# output = conn.commit()
# print(output)

# Return to exec mode
output = conn.exit_config_mode()
print(output)

# Close connection
conn.disconnect()
