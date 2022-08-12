#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig wlx984827e68cf7 down", shell=True)
subprocess.call("ifconfig wlx984827e68cf7 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig wlx984827e68cf7 up", shell=True)