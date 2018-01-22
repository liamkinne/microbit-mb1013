from microbit import *

class mb1013_serial:
	def __init__(self, pin_rx, pin_enable):
		self.pin_rx = pin_rx
		self.pin_enable = pin_enable

	def get(self):
		uart.init(baudrate=9600,bits=8,parity=None,stop=1,rx=pin0)
		pin1.write_digital(True)
		retrun str(uart.readline())[1:]
		uart.init(115200)
		pin1.write_digital(False)

class mb1013_analog:
	def __init__(self, pin_analog, pin_enable=None):
		self.pin_analog = pin_analog
		self.pin_enable = pin_enable

		self.pin_analog.read_analog()

	def get(self):
		if self.pin_enable != None: pin_enable.write_digital(True)

		reading = self.pin_analog.read_analog() * 5

		if self.pin_enable != None: pin_enable.write_digital(False)

		return reading