from larpix.larpix import Controller, Packet
from larpix.io.fakeio import FakeIO 
from larpix.logger.stdout_logger import StdoutLogger 

print('\n')
print('\n')

# Controller
##########################################################################################
controller = Controller()
controller.io = FakeIO()
controller.logger = StdoutLogger(buffer_length = 0)
controller.logger.enable()
##########################################################################################

chip1 = controller.add_chip('1-1-1')
chip1.config.global_threshold = 25
print(controller.write_configuration('1-1-1'))

print('\n')
print('\n')

packet = Packet(b'\x04\x14\x80\xc4\x03\xf2 ')
packet_bytes = packet.bytes()
pretend_input = ([packet], packet_bytes)
controller.io.queue.append(pretend_input)
controller.run(0.05, 'test run')
print(controller.reads[0])

controller.logger.disable()

print('\n')
print('\n')

# what does all of this mean?

# LArPix Controller (See Jupyter Notebook to follow along)
#	# translates high-level python code into low-level ASIC code between the user 
#	  and the pixelated sensors (ASIC - Application Specific Integrated Circuit)
#	# communicates between user and ASICs via IO interface
#			# SerialPort
#			# ZMQ_IO
#			# FakeIO
#				# imitation of a real IO interface (for testing purposes)
#				# directs output to stdout and prints the output without any return function
#				# takes in input from a manually updated queue
#	# StdoutLogger 
#			# mimics the real logger interface for testing, similar to FakeIO
#			# prints records of read/write commands to buffer_length packets
#			# requires enabling the logger interface before storing
#			# At the end of each session, the logger must be disabled
#
# LArPix Chips (See Jupyter Notebook to follow along)
#	# Chip objects represent actual ASIC's
#	# For each ASIC to communicate with, create a Chip object and add it to LArPix controller
#	# chip_key field specifies info for controller.io to route packets to/from the chip
#	# for each larpix.io class, the chip key consists of 3 1-byte integer values, specified as:
#			# IO Group:
#				# Highest Layer
#				# represents a control sys that communicates with multiple IO channels
#			# IO Channel:
#				# Middle Layer
#				# represents a single MOSI/MISO pair
#			# Chip ID:
#				# Lowest Layer
#				# represents a single chip on a MISO/MOSI network
#	# To interact with chip keys directly, use a valid keystring ('#-#-#')
