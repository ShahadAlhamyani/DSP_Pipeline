import math 
from generate_iq import gererate_mock_iq_file
from read_iq import read_iq
from ChannelSimulator import Channel
from iq_analyzer import analyzer


class Transmitter:
    def __init__(self,sample_rate):
        self.sample_rate = sample_rate
       

    def transmitter(self):
        signal = gererate_mock_iq_file() # save output(mock_dsatellite_signal.bin) of the fun here
        sample = read_iq(signal)
        channel = Channel(sample)
        noisy_samples = channel.inject_awgn(20)
        analyzer(noisy_samples,self.sample_rate) # insert file and rate to analyzer fun


        


#---------main-----------
sample_rate = 1000      # 1 kHz it was 2048000
tran = Transmitter (sample_rate)
tran.transmitter()
