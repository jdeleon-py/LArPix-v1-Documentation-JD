class Data_Manipulated_Hex:
    
    ''' Timestamp: 123456789 '''
    data_packet1 = b'\x02\x91\x15\xcd[\x07\x00\x00' # ADC Data: 0
    data_packet2 = b'\x02\x91\x15\xcd[\x07d\x00'    # ADC Data: 100
    data_packet3 = b'\x02\x91\x15\xcd[\x07\xc8\x00' # ADC Data: 200
    data_packet4 = b'\x02\x91\x15\xcd[\x07\xff\x00' # ADC Data: 255
        
        
class Time_Manipulated_Hex:
    
    ''' Dataword: 133 '''
    time_packet0 = b'\x02\x91\x80\xf0\xfa\x02\x85\x00' # Timestamp: 50000000
    time_packet1 = b'\x02\x91\x00\xe1\xf5\x05\x85\x00' # Timestamp: 100000000
    time_packet2 = b'\x02\x91\x80\xd1\xf0\x08\x85\x00' # Timestamp: 150000000
    time_packet3 = b'\x02\x91\x00\xc2\xeb\x0b\x85\x00' # Timestamp: 200000000
    time_packet4 = b'\x02\x91\x80\xb2\xe6\x0e\x85\x00' # Tiemstamp: 250000000
    time_packet5 = b'\x02\x91\x00\xa3\xe1\x11\x85\x00' # Timestamp: 300000000
    time_packet6 = b'\x02\x91\x80\x93\xdc\x14\x85\x00' # Timestamp: 350000000
    time_packet7 = b'\x02\x91\x00\x84\xd7\x17\x85\x00' # Timestamp: 400000000
    time_packet8 = b'\x02\x91\x80t\xd2\x1a\x85\x00'    # Timestamp: 450000000
    time_packet9 = b'\x02\x91\x00e\xcd\x1d\x85\x00'    # Timestamp: 500000000
    
        
class Hex_Routine1:
    
    packet0 = b'\x02\x91\x80\xf0\xfa\x02\x00\x00' # Timestamp: 50000000,  Data: 0
    packet1 = b'\x02\x91\x00\xe1\xf5\x05\x00\x00' # Timestamp: 100000000, Data: 0
    packet2 = b'\x02\x91\x80\xd1\xf0\x08\x00\x00' # Timestamp: 150000000, Data: 0
    packet3 = b'\x02\x91\x00\xc2\xeb\x0b\xff\x00' # Timestamp: 200000000, Data: 255
    packet4 = b'\x02\x91\x80\xb2\xe6\x0e\xff\x00' # Tiemstamp: 250000000, Data: 255
    packet5 = b'\x02\x91\x00\xa3\xe1\x11\xff\x00' # Timestamp: 300000000, Data: 255
    packet6 = b'\x02\x91\x80\x93\xdc\x14\xff\x00' # Timestamp: 350000000, Data: 255
    packet7 = b'\x02\x91\x00\x84\xd7\x17\x00\x00' # Timestamp: 400000000, Data: 0
    packet8 = b'\x02\x91\x80t\xd2\x1a\x00\x00'    # Timestamp: 450000000, Data: 0
    packet9 = b'\x02\x91\x00e\xcd\x1d\x00\x00'    # Timestamp: 500000000, Data: 0