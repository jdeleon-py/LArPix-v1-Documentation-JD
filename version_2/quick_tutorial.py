from larpix.larpix import Controller, Packet
from larpix.io.fakeio import FakeIO 
from larpix.logger.stdout_logger import StdoutLogger 

### Run this program to output a sample. If there are no errors when running this program, you are all set.
### Notes of the code (Controller, Chips, and Packet modules are located in the Github file, quick_tutorial_explanation.py)
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
# Output: Record: [ Chip key: 1-1-5 | Chip: 5 | Config write | Register: 0 | Value:  16 | Parity: 0 (valid: True) ]
#                 [ Chip key: 1-1-5 | Chip: 5 | Config write | Register: 1 | Value:  16 | Parity: 0 (valid: True) ]
#                 [ Chip key: 1-1-5 | Chip: 5 | Config write | Register: 2 | Value:  16 | Parity: 0 (valid: True) ]
#                 [ Chip key: 1-1-5 | Chip: 5 | Config write | Register: 3 | Value:  16 | Parity: 1 (valid: True) ]
# 63 different registers (0-62) in a list is output to the screen
# value varies from 0 to 255
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
# Output: Record: [ Chip key: None | Chip: 1 | Data | Channel: 5 | Timestamp: 123456 | ADC data: 120 | FIFO Half: False | FIFO Full: False | Parity: 1 (valid: True) ]
##########################################################################################

#controller.logger.disable() # For this sample, the disable() method is not needed, but may be useful in the future.

print('\n')
print('\n')
