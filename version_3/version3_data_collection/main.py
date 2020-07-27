from larpix import Controller, Packet_v2
from larpix.io import FakeIO
from larpix.logger import StdoutLogger
import h5py
import numpy as np
import matplotlib.pyplot as plt
from v1_data_collector import Data_Collection 
from v1_packet_database import Data_Manipulated_Hex, Time_Manipulated_Hex, Hex_Routine1

if __name__ == "__main__":
	test = Data_Collection(name_of_file = 'test_file14_06_02_2020.h5', chip_id = '1-1-2', buffer_length = 10)
	
	test.data_trial(iteration = 0, packet_key = Hex_Routine1.packet0, time = 1, message = 'test')
	test.data_trial(iteration = 1, packet_key = Hex_Routine1.packet1, time = 1, message = 'test')
	test.data_trial(iteration = 2, packet_key = Hex_Routine1.packet2, time = 1, message = 'test')
	test.data_trial(iteration = 3, packet_key = Hex_Routine1.packet3, time = 1, message = 'test')
	test.data_trial(iteration = 4, packet_key = Hex_Routine1.packet4, time = 1, message = 'test')
	test.data_trial(iteration = 5, packet_key = Hex_Routine1.packet5, time = 1, message = 'test')
	test.data_trial(iteration = 6, packet_key = Hex_Routine1.packet6, time = 1, message = 'test')
	test.data_trial(iteration = 7, packet_key = Hex_Routine1.packet7, time = 1, message = 'test')
	test.data_trial(iteration = 8, packet_key = Hex_Routine1.packet8, time = 1, message = 'test')
	test.data_trial(iteration = 9, packet_key = Hex_Routine1.packet9, time = 1, message = 'test')

	test.retrieve_data()

	for i in range(0, 10):
	    test.data_specs(index = i)
	    print('\n')

	test.read_file_data()

	test.plot_data(title = 'Data Gathering of Chip 1-1-2')