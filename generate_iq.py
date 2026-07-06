import math
import struct


# this code generate pure IQ signals, therefore i need to add channel


def gererate_mock_iq_file(filename = "mock_dsatellite_signal.bin"
    ,duration_sec = 0.1,sample_rate = 20000, signal_freq = 1000):
   
    total_sample = int (sample_rate * duration_sec)

    with open(filename, "wb") as f:
        for n in range(total_sample):
            theta = 2.0 * math.pi * signal_freq * n / sample_rate

            i_val = math.cos(theta)
            q_val = math.sin(theta)

            packed_bytes = struct.pack('ff', i_val, q_val) 
            f.write(packed_bytes)

    return "mock_dsatellite_signal.bin"
        



#------main------
gererate_mock_iq_file()    