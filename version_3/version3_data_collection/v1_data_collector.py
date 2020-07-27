from larpix import Controller, Packet_v2
from larpix.io import FakeIO
from larpix.logger import StdoutLogger
import h5py
import numpy as np
import matplotlib.pyplot as plt


class Data_Collection:

    def __init__(self, name_of_file, chip_id, buffer_length):
        self.data_packets = Data_Manipulated_Hex()
        self.time_packets = Time_Manipulated_Hex()
        
        self.save_to_file = name_of_file
        self.chip_id = chip_id
        self.buffer_length = buffer_length
        
        self.controller = Controller()
        self.controller.io = FakeIO()
        self.controller.logger = StdoutLogger(buffer_length = self.buffer_length)

        self.controller.logger.enable()
        # enable a h5py file to write out to
        self.file_write = h5py.File(self.save_to_file, 'w')

        self.chip = self.controller.add_chip(self.chip_id, version = 2)


    def _chip_modification(self, g_threshold, per_reset = None, channel_msk = None):
        chip.config.global_threshold = g_threshold
        chip.config.periodic_reset = per_reset
        #chip.config.channel_mask = channel_msk

        print("Writing chip configuration...")
        print(self.controller.write_configuration(self.chip_id))


    def data_trial(self, iteration, packet_key, time, message):
        packet = Packet_v2(packet_key)
        packet_bytes = packet.bytes()

        trial_input = ([packet], packet_bytes)
        self.controller.io.queue.append(trial_input)

        print('Data is collecting...')
        self.controller.run(time, message)
        print('Data collected!')
        
        print('Converting data to be written out to file...')
        converted_data = self._convert_data(trial_index = iteration)
        print(converted_data)
        self.file_write.create_dataset('packet' + str(iteration), data = converted_data)
        
        
    def _convert_data(self, trial_index):
        data_arr = []
        run = self.controller.reads[trial_index]
        packet_info = run[0]
        
        data_arr = np.array([packet_info.packet_type, 
                             packet_info.chip_id,
                             packet_info.parity,
                             packet_info.downstream_marker,
                             packet_info.channel_id,
                             packet_info.dataword,
                             packet_info.timestamp,
                             packet_info.trigger_type,
                             packet_info.local_fifo,
                             packet_info.shared_fifo,
                             packet_info.register_address,
                             packet_info.register_data])
        
        return data_arr

    
    def _end_collection_process(self):
        self.controller.logger.disable()
        # close the h5py file that is being written
        self.file_write.close()


    def retrieve_data(self):
        self._end_collection_process()

        print("Completed: This is the collected data...")
        print(self.controller.reads)

        
    def data_specs(self, index):
        run = self.controller.reads[index]
        packet_data = run[0] # >>> bitarray('00')
        
        print('Packet Type: ' + str(packet_data.packet_type))  # unique in that it gives the bits representation
        print('Chip ID: ' + str(packet_data.chip_id)) # all other properties return Python numbers
        print('Chip Key: ' + str(packet_data.chip_key)) # key for association to a unique chip (can be None)
        print('Parity: ' + str(packet_data.parity))
        print('Downstream Marker: ' + str(packet_data.downstream_marker))

        # data packets
        print('Channel ID: ' + str(packet_data.channel_id))
        print('Dataword: ' + str(packet_data.dataword))
        print('Timestamp: ' + str(packet_data.timestamp))
        print('Trigger Type: ' + str(packet_data.trigger_type))
        print('Local FIFO: ' + str(packet_data.local_fifo))
        print('Shared FIFO: ' + str(packet_data.shared_fifo))

        # config packets
        print('Register Address: ' + str(packet_data.register_address))
        print('Register Data: ' + str(packet_data.register_data))
        
        
    def read_file_data(self):
        data = []
        file = h5py.File(self.save_to_file, 'r')
        keys = list(file.keys())
        print(keys)
        
        for i in range(0, len(keys)):
            # print(file[keys[i]][:])
            data.append(file[keys[i]][:])
            
        #print(file['packets'][0])
        #returned_values = file['packets'][0]
        #self.data_array = returned_values
        
        file.close()
        return data

       
    def plot_data(self, title): # ADC data vs timestamp scatter plot
        '''
        This may be considered an extraneous function and most likely will be called manually in practice.
        (Not every trial will need a plot and multiple trials of varying lengths and entries may share one plot)
        '''
        data_unadjusted = self.read_file_data()
        timestamp_data = []
        adc_data = []
        
        for i in range(0, len(data_unadjusted)):
            timestamp_data.append(data_unadjusted[i][6])
            adc_data.append(data_unadjusted[i][5])
        
        plt.title(title)
        plt.xlabel("Timestamp")
        plt.ylabel("ADC Data")
        plt.scatter(timestamp_data, adc_data, color = 'black', marker = 'v')
        plt.show()