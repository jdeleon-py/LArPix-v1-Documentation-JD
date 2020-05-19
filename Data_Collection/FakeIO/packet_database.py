# Generated Fake Data (use only for the FakeIO class)
# control hex string: b'\x04\x14\x80\xc4\x03\xf2 '

# Each hex string below is generated as variants from the hex string above.
# The 'Control' Hex String has a ADC data value of 120 and a timestamp of 123456.
# These packets simulate a specific data value in a specific timestamp from a specific channel.

# Either the data value or the timestamp value is variable, with constants being:
# Chip: 1
# Channel: 5
# Valid Parity Bit: True

class Data_Manipulated_Hex:

	def __init__(self):
		''' Timestamp: 123456 '''
		self.data_packet1 = b'\x04\x14\x80\xc4\x03\x02 ' # ADC Data: 0
		self.data_packet2 = b'\x04\x14\x80\xc4\x032 '	 # ADC Data: 24
		self.data_packet3 = b'\x04\x14\x80\xc4\x03R '	 # ADC Data: 40
		self.data_packet4 = b'\x04\x14\x80\xc4\x03b '	 # ADC Data: 48
		self.data_packet5 = b'\x04\x14\x80\xc4\x03\x92 ' # ADC Data: 72
		self.data_packet6 = b'\x04\x14\x80\xc4\x03\xa2 ' # ADC Data: 80
		self.data_packet7 = b'\x04\x14\x80\xc4\x03\xc2 ' # ADC Data: 96
		self.data_packet8 = b'\x04\x14\x80\xc4\x03\xf2 ' # ADC Data: 120


class Time_Manipulated_Hex:

	def __init__(self):
		''' ADC Data: 120 '''
		self.time_packet1 = b'\x04\x14\x80\x04\x03\xf2 ' # Timestamp: 98880
		self.time_packet2 = b'\x04\x14\x804\x03\xf2 '	 # Timestamp: 105024
		self.time_packet3 = b'\x04\x14\x80T\x03\xf2 '	 # Timestamp: 109120
		self.time_packet4 = b'\x04\x14\x80d\x03\xf2 ' 	 # Timestamp: 111168
		self.time_packet5 = b'\x04\x14\x80\x94\x03\xf2 ' # Timestamp: 117312
		self.time_packet6 = b'\x04\x14\x80\xa4\x03\xf2 ' # Timestamp: 119360
		self.time_packet7 = b'\x04\x14\x80\xc4\x03\xf2 ' # Timestamp: 123456
		self.time_packet8 = b'\x04\x14\x80\xf4\x03\xf2 ' # Timestamp: 129600
		
