# This tutorial is similar to that of tutorial 2,
# the main difference being that this tutorial is utilizing larpix-control v3.1.1

from larpix import Controller, Packet_v2
from larpix.io import FakeIO
from larpix.logger import StdoutLogger

controller = Controller()
controller.io = FakeIO()
controller.logger = StdoutLogger(buffer_length = 0)
controller.logger.enable()
chip1 = controller.add_chip('1-1-2', version = 2)  # (access key)
chip1.config.threshold_global = 25
controller.write_configuration('1-1-2', chip1.config.register_map['threshold_global']) # chip key, register 64

#[ Key: 1-1-2 | Chip: 2 | Upstream | Write | Register: 64 | Value: 25 | Parity: 1 (valid: True) ]
#Record: [ Key: 1-1-2 | Chip: 2 | Upstream | Write | Register: 64 | Value: 25 | Parity: 1 (valid: True) ]

packet = Packet_v2(b'\x02\x91\x15\xcd[\x07\x85\x00')
packet_bytes = packet.bytes()
pretend_input = ([packet], packet_bytes)
controller.io.queue.append(pretend_input)
controller.run(0.05, 'test run')

#Record: [ Key: None | Chip: 2 | Downstream | Data | Channel: 5 | Timestamp: 123456789 | First packet: 0 | Dataword: 145 | Trigger: normal | Local FIFO ok | Shared FIFO ok | Parity: 0 (valid: True) ]
print(controller.reads[0])

print('\n')

run = controller.reads[0]
packet = run[0]

# all packets
print('Packet Type: ' + str(packet.packet_type))  # unique in that it gives the bits representation
print('Chip ID: ' + str(packet.chip_id)) # all other properties return Python numbers
print('Chip Key: ' + str(packet.chip_key)) # key for association to a unique chip (can be None)
print('Parity: ' + str(packet.parity))
print('Downstream Marker: ' + str(packet.downstream_marker))

# data packets
print('Channel ID: ' + str(packet.channel_id))
print('Dataword: ' + str(packet.dataword))
print('Timestamp: ' + str(packet.timestamp))
print('Trigger Type: ' + str(packet.trigger_type))
print('Local FIFO: ' + str(packet.local_fifo))
print('Shared FIFO: ' + str(packet.shared_fifo))

# config packets
print('Register Address: ' + str(packet.register_address))
print('Register Data: ' + str(packet.register_data))

