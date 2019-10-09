#Nocturnalnetworking.com
#This script uses netmiko to create vlans
from netmiko import ConnectHandler
#Dictionaries for the switches 
SW1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.72',
	'username': 'kelvin',
	'password': 'cisco',
	
}

SW2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.82',
	'username': 'kelvin',
	'password': 'cisco',
}

SW3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.83',
	'username': 'kelvin',
	'password': 'cisco',
}

SW4 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.84',
	'username': 'kelvin',
	'password': 'cisco',
}
#A list of the dictionaries
switches = [SW1, SW2, SW3, SW4]
#Loops through the devices in the switches list and creates the Vlans.
for devices in switches:
	net_connect = ConnectHandler(**devices)
	for n in range (2,5):
		print ("Creating VLAN " + str(n))
		config_commands = ['vlan ' + str(n), 'name NocNet_VLAN ' + str(n)]
		output = net_connect.send_config_set(config_commands)
		print (output)
