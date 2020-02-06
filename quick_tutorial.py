from larpix.larpix import Controller, Packet
from larpix.io.fakeio import FakeIO 
from larpix.logger.stdout_logger import StdoutLogger 

### Run this program to output a sample. If there are no errors when running this program, you are all set.
### The sample output is a series of data information. Translating the data will be included in the near future.

print('\n') # new lines for spacing out the printed items for easier analysis
print('\n')

# Controller
##########################################################################################
controller = Controller()
controller.io = FakeIO()
controller.logger = StdoutLogger(buffer_length = 0)
controller.logger.enable()
##########################################################################################

# Chips
##########################################################################################
chip1 = controller.add_chip('1-1-5')
chip1.config.global_threshold = 25
print(controller.write_configuration('1-1-5'))
##########################################################################################

print('\n')
print('\n')

# Inclusion of Packets
##########################################################################################
packet = Packet(b'\x04\x14\x80\xc4\x03\xf2 ')
packet_bytes = packet.bytes()
pretend_input = ([packet], packet_bytes)
controller.io.queue.append(pretend_input)
controller.run(0.05, 'test run')
print(controller.reads[0])
##########################################################################################

#controller.logger.disable() # For this sample, the disable() method is not needed, but may be useful in the future.

print('\n')
print('\n')
