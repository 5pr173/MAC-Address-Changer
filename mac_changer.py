#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option('-r', '--run', dest='mode', help='Select the mode to run the script in: command or terminal')
parser.add_option('-i', '--interface', dest='interface', help='The interface of the device you want to change the MAC address of.')
parser.add_option('-m', '--mac', dest='new_mac', help='The MAC address that you want to be your new MAC address.')

(options, args) = parser.parse_args()

if options.mode == 'command':
    interface_command = options.interface
    new_mac_command = options.new_mac

    print ('[+] Changin the MAC address for ' + interface_command + ' to ' + new_mac_command)

    subprocess.call(['sudo', 'ifconfig', interface_command, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface_command, 'hw', 'ether', new_mac_command])
    subprocess.call(['sudo', 'ifconfig', interface_command, 'up'])

elif options.mode == 'terminal':
    interface_terminal = input('Interface > ')
    new_mac_terminal = input('MAC address > ')

    print('[+] Changing the MAC address for ' + interface_terminal + ' to ' + new_mac_terminal)

    subprocess.call(['sudo', 'ifconfig', interface_terminal, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface_terminal, 'hw', 'ether', new_mac_terminal])
    subprocess.call(['sudo', 'ifconfig', interface_terminal, 'up'])
else:
    print('Please the --help command to see how to run this program.')