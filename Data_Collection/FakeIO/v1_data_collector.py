# This is a rough setup going through the process of a trial of data collection.
# This particular file uses an OOP structure to make the process as user-friendly as possible.
# The trial will be the initialization of the object and the functions that follow will be ways in which the 
# data can be taken, received, written to a file, and plotted.
# Reminder: for the FakeIO interface, the data collected can be only yield one value in one snapshot of time from a specific channel.

from larpix.larpix import *
from larpix.io.fakeio import FakeIO
from larpix.logger.h5_logger import HDF5Logger
import h5py
import numpy as np
import matplotlib.pyplot as plt
import packet_database as p # <v1_packet_database>

class Data_Collection:

    def __init__(self, name_of_file, chip_id):
        self.data_packets = p.Data_Manipulated_Hex()
        self.time_packets = p.Time_Manipulated_Hex()
        
        self.save_to_file = name_of_file
        self.chip_id = chip_id
        self.controller = Controller()
        self.controller.io = FakeIO()
        self.controller.logger = HDF5Logger(filename = self.save_to_file, buffer_length = 10000)

        self.controller.logger.enable()

        self.chip = self.controller.add_chip(self.chip_id)
        
        self.data_array = []


    def chip_modification(self, g_threshold, per_reset = None, channel_msk = None):
        key = chip_id
        chip.config.global_threshold = g_threshold
        chip.config.periodic_reset = per_reset
        #chip.config.channel_mask = channel_msk

        print("Writing chip configuration...")
        print(self.controller.write_configuration(key))


    def data_trial(self, packet_key, time, message):
        packet = Packet(packet_key)
        packet_bytes = packet.bytes()

        trial_input = ([packet], packet_bytes)
        self.controller.io.queue.append(trial_input)

        print("Data is collecting...")
        self.controller.run(time, message)
        print("Data collected!")


    def _end_collection_process(self):
        self.controller.logger.disable()


    def retrieve_data(self):
        self._end_collection_process()

        print("Completed: This is the collected data...")
        print(self.controller.reads)

        
    def data_specs(self, index):
        run = self.controller.reads[index]

        packet_data = run[index] # >>> bitarray('00')
        
        # print("Packet Type: " + str(packet_data.packet_type)) # >>> 1
        print("Chip ID: " + str(packet_data.chipid)) # >>> 1
        print("Chip Key: " + str(packet_data.chip_key))
        print("Parity Bit Value: " + str(packet_data.parity_bit_value)) # >>> 1
        print("Channel ID: " + str(packet_data.channel_id)) # >>> 5
        print("Dataword: " + str(packet_data.dataword)) # >>> 120
        print("Timestamp: " + str(packet_data.timestamp)) # >>> 123456
        print("Fifo Full Flag: " + str(packet_data.fifo_full_flag)) # >>> 0 (1 or 0)
        print("Fifo Half Flag: " + str(packet_data.fifo_half_flag)) # >>> 0 (1 or 0)
        print("Register Address: " + str(packet_data.register_address)) # >>> 5
        print("Register Data: " + str(packet_data.register_data)) # >>> 32
        print("Test Counter: " + str(packet_data.test_counter)) # >>> 20601
        
    def read_file(self):
        file = h5py.File(self.save_to_file, 'r')
        
        print(list(file.keys()))
        print(file['packets'][0])
        returned_values = file['packets'][0]
        self.data_array = returned_values
        
        file.close()
        
    def plot_data(self, title): # ADC data vs timestamp scatter plot
        refined_data_arr = [self.data_array[6], self.data_array[7]]
        
        plt.title(title)
        plt.xlabel("Timestamp")
        plt.ylabel("ADC Data")
        plt.scatter(refined_data_arr[0], refined_data_arr[1], color = 'black')
        plt.show()
        

# Example of a run:
'''
trial = Data_Collection(name_of_file = 'trial001', chip_id = '1-1-5')

trial.data_trial(packet_key = b'\x04\x14\x80\xc4\x032 ', time = 0.05, message = 'trial001') #p.data_packet2

trial.retrieve_data()

trial.data_specs(index = 0) # since there is only one packet available

trial.read_file()

trial.data_array

trial.plot_data(title = "Channel 5 Snapshot")
'''
