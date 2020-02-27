#Nocturnalnetworking.com
#This script uses netmiko to create vlans
from netmiko import ConnectHandler
#This part makes the script a little bit more secure by asking the user to enter the password instead of storing it in the script.
from getpass import getpass
ask = getpass()
#Dictionaries for the switches 

SW1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.51',
	'username': 'kelvin',
	'password': ask,
	
}

SW2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.52',
	'username': 'kelvin',
	'password': ask,
}

SW3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.53',
	'username': 'kelvin',
	'password': ask,
}

SW4 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.54',
	'username': 'kelvin',
	'password': ask,
}

SW5 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.55',
	'username': 'kelvin',
	'password': ask,
}
#A list of the dictionaries
switches = [SW1, SW2, SW3, SW4,SW5]
#Loops through the devices in the switches list and creates the Vlans.
for devices in switches:
	net_connect = ConnectHandler(**devices)
	for n in range (2,5):
		print ("Creating VLAN " + str(n))
		config_commands = ['vlan ' + str(n), 'name NocNet_VLAN ' + str(n)]
		output = net_connect.send_config_set(config_commands)
		print (output)
