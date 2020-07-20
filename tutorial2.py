# In this tutorial, the same imitation data from quick_tutorial1.py will be used, however this time,
# data will be stored into a file for processing with a numpy-based library

# This tutorial can be completed using any IDE running Python. Preferably, your machine's terminal is the ideal platform
# Eventually, all data collection will be performed using the machine terminal

# Start by importing all the necessary libraries and packages
from larpix.larpix import *
from larpix.io.fakeio import FakeIO
from larpix.logger.h5_logger import HDF5Logger
import h5py
import numpy as np

# Initiate the controller, io interface, and logging system (to store data)
controller1 = Controller()
controller1.io = FakeIO()
controller1.logger = HDF5Logger(filename = 'test001', buffer_length = 100)

# Start tracking all communications with the logging system
controller1.logger.enable()

# Initiate the chip, we will be using a chip with chip key '1-2-3'

#Does a chip need to be initiated at all??
#   - For this FakeIO-based simulation, initiating a Chip object is not necessary to get the results we desire.
#   - However, when we start testing with real data using the ZMQ_IO interface, Chip objects are necessary.
#   - For the sake of information, I will go through the process of initiating a Chip object
chip1 = controller1.add_chip('1-0-0')

chip1.config.global_threshold = 25 # Config is a method to set parameters to our Chip object
chip1.config.periodic_reset = 1 # The global_threshold method may be the most important one for us to use.
chip1.config.channel_mask[20] = 1 # These parameters are not required for the functionality of this tutorial

controller1.write_configuration('1-0-0') # Configures all chip registers with the chip ID '1-2-3' to prepare for testing

# Now, prepare an input to be put into a queue for testing.
packet1 = Packet(b'\x04\x14\x80\xc4\x03\xf2 ') # An input packet is defined with a specific bytestream necessary for this test
packet1_bytes = packet1.bytes()

trial_input = ([packet1], packet1_bytes)
controller1.io.queue.append(trial_input)

# .run(duration(seconds), message) Allows for the board to start data collection then stop data collection 0.05 seconds later
# This has completed the 'gathering data process' so therefore cease all communications from the ASIC's after
controller1.run(0.05, 'test run #1')
controller1.logger.disable()

# Your computer's memory has now stored a trial run of data
print(controller1.reads)
# Output should read: >>> [<PacketCollection with 1 packets, read_id 0, "test run for 0.05 second">]

# Access the details of the trial run
print(controller1.reads[0])
# Output should read: >>> [ Chip key: None | Chip: 1 | Data | Channel: 5 | Timestamp: 123456 | ADC data: 120 | FIFO Half: False | FIFO Full: False | Parity: 1 (valid: True) ]

# Once data is stored in the controller, it is available in the reads attribute as a list of all data runs. 
run1 = controller1.reads[0]

print(run1[0]) # Packet object
print(run1[0, 'bits']) # String representation of bits in Packet
# Output: >>> '10000011 11001000 00001111 00010010 00000000 01010000 000100'
print(run1[10:30]) # Print 20 middle packets from the trial run, or index a specified amount to prevent endless scrolling

# Individual LArPix Packets to inspect/modify
packet_data = run1[0] # >>> bitarray('00')
print(packet_data.packet_type) # >>> 1
print(packet_data.chipid) # >>> 1
print(packet_data.chip_key)
print(packet_data.parity_bit_value) # >>> 1
print(packet_data.channel_id) # >>> 5
print(packet_data.dataword) # >>> 120
print(packet_data.timestamp) # >>> 123456
print(packet_data.fifo_full_flag) # >>> 0 (1 or 0)
print(packet_data.fifo_half_flag) # >>> 0 (1 or 0)
print(packet_data.register_address) # >>> 5
print(packet_data.register_data) # >>> 32
print(packet_data.test_counter) # >>> 20601

# Now that we know how to read this data, how can we export this to a file?
datafile = h5py.File('test001')

# With every file, there are keys that access certain parts of the file
print(list(datafile.keys()))
# Output: >>> ['_header', 'messages', 'packets'] (the 'packets' key is what we are interested in)

print(datafile['packets'])
# Output: >>> <HDF5 dataset "packets": shape (1,), type "|V55">

print(datafile['packets'][0]) # accesses the raw values of the first packet
# Output: >>> (b'None', 0, 1, 1, 1, 5, 123456, 120, 0, 0, 0, 0, 0, 0) (these are the raw values from the trial of data that was just taken)
print(datafile['packets'][1])
print(datafile['packets'][:])

raw_values = datafile['packets'][:10] # first ten entries of the packet sample

# Use numpy to transform the raw data into organized data, in which entire columns under a datatype can be accessed.
# Disclaimer: this tutorial only has one Packet to test with
packet_repr = raw_values[0:1] # list with one element
print(packet_repr['chip_key']) # chip key for packet, e.g. b'1-1-246'
print(packet_repr['adc_counts']) # list of ADC values for each packet
print(packet_repr.dtype) # description of data type (with names of each column)

# One layer back, all sliced raw_values can be investigated with the same tags
print(raw_values['adc_counts'])
print(raw_values['register'])
print(raw_values['direction'])
print(raw_values['value'])

# Masking Exercise
print(raw_values['adc_counts'][raw_values['register'] % 2 == 0]) # 5 of the ten values will be printed

# Close the file
datafile.close()
