# This file is a continuation of a previous tutorial file, quick_tutorial.py
# This file should provide a brief explanation of each of the parts(modules) involved in the code.


# LArPix CONTROLLER
# - translates high-level python code into low-level ASIC code between the user 
#	  and the pixelated sensors (ASIC - Application Specific Integrated Circuit)
#	- communicates between user and ASICs via IO interface
#			# SerialPort
#			# ZMQ_IO
#       - the second level of experimenting and testing
#       - To be continued...
#			# FakeIO
#				- the first level of experimenting and testing
#       - imitation of a real IO interface (for testing purposes)
#				- directs output to stdout and prints the output without any return function
#				- takes in input from a manually updated queue
#	- StdoutLogger 
#			# mimics the real logger interface for testing, similar to FakeIO
#			# prints records of read/write commands to buffer_length packets
#			# requires enabling the logger interface before storing
#			# At the end of each session, the logger must be disabled
#
##########################################################################################
controller = Controller() ### initiates a Controller Object

controller.io = FakeIO() ### initiates the Controller's ability to handle input and output

controller.logger = StdoutLogger(buffer_length = 0) ### initiates the Controller's ability to store data
### buffer_length is an argument that represents the number of packets

controller.logger.enable() ### starts tracking all communications 
### after all data has been collected and stored, the logger.disable() method is used to cleanse the system of all loose data
##########################################################################################


# LArPix CHIPS
#	- Chip objects represent actual ASIC's
#	- For each ASIC to communicate with, create a Chip object and add it to LArPix controller
#	- chip_key field specifies info for controller.io to route packets to/from the chip
#	- for each larpix.io class, the chip key consists of 3 1-byte integer values, specified as:
#			# IO Group:
#				- Highest Layer
#				- represents a control sys that communicates with multiple IO channels
#			# IO Channel:
#				- Middle Layer
#				- represents a single MOSI/MISO pair
#			# Chip ID:
#				- Lowest Layer
#				- represents a single chip on a MISO/MOSI network
#	- To interact with chip keys directly, use a valid keystring ('#-#-#')
#
##########################################################################################
chip1 = controller.add_chip('1-1-5') ### activates a chip to be used for testing, (<IO Group>, <IO Channel>, <Chip ID>)
chip1.config.global_threshold = 25 
print(controller.write_configuration('1-1-5'))
##########################################################################################
