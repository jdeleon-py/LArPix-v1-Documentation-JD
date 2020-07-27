from larpix import Controller, Packet_v2
from larpix.io import FakeIO
from larpix.logger import StdoutLogger

class Test:
    
    def __init__(self, chip_id):
        self.chip_id = chip_id
        
        self.controller = Controller()
        self.controller.io = FakeIO()
        self.controller.logger = StdoutLogger(buffer_length = 0)
        
        self.controller.logger.enable()
    
        self.chip = self.controller.add_chip(self.chip_id, version = 2)
        self.chip.config.threshold_global = 25

        
    def _write_config(self):
        self.controller.write_configuration(self.chip_id)

        
    def trial(self, packet_in, time, message):
        packet = Packet_v2(packet_in)
        packet_bytes = packet.bytes()
        pretend_input = ([packet], packet_bytes)
        
        self.controller.io.queue.append(pretend_input)
        self.controller.run(time, message)
        
    
    def _end_collection_process(self):
        self.controller.logger.disable()
        
    
    def read_data(self, index):
        self._end_collection_process()
        
        print(self.controller.reads[index])
        
        run = self.controller.reads[index]
        packet = run[index]

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

if __name__ == '__main__':
    test = Test(chip_id = '1-1-2')

    test._write_config()

    test.trial(packet_in = b'\x02\x91\x15\xcd[\x07\x85\x00', time = 0.05, message = 'test')

    test.read_data(index = 0)