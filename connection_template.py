####DEPENDENCIES####

from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
import exceptions
import math
import argparse #To import some values from command line and use it on our python script

#####################functions####
def connectMyCopter():
	parser=argparse.ArgumentParser(description='commands')
	parser.add_argument('--connect') ##Sec
	args = parser.parse_args()

	connection_string=args.connect

	vehicle=connect(connection_string,wait_ready=True) #To connect the vehicle using ip address and wait ready means it will pass command only when the connection is set up.

	return vehicle

###>> pythonconnection_template.py --connect 127.0.0.1:14550

#main execution#
vehicle =connectMyCopter()
