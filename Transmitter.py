import math 
from generate_iq import gererate_mock_iq_file
from read_iq import read_iq
from ChannelSimulator import Channel
from iq_analyzer import analyzer


class Transmitter:
    def __init__(self,sample_rate):
        self.sample_rate = sample_rate

       

    def transmitter(self):
        signal = gererate_mock_iq_file() 
        sample = read_iq(signal) # already saved in signal just comment them in the file
        channel = Channel(sample) # when passing values be carefull casue there are more than method
        result = channel.inject_awgn(20)  #i should pass values for sample_rate, doppler_hz 
        noisy_samples = result["noisy_samples"]
        analyzer(noisy_samples, self.sample_rate)


    def report(self):
        open("traced_iq_output.txt", "w").close()
        
        signal = gererate_mock_iq_file()
        sample = read_iq(signal)

        self.print_samples("Original Symbols", sample)

        channel = Channel(sample)

        doppler = channel.inject_doppler()
        self.print_samples("Inject Doppler", doppler["doppler_packet"])

        awgn = channel.inject_awgn(20)
        self.print_samples("Inject AWGN", awgn["inject_awgn_packet"])

        analyzer_result = analyzer(
            awgn["noisy_samples"],
            self.sample_rate
        )

        self.print_samples("Analyzer", analyzer_result)


            
    def print_samples(self, stage_name, parameters,
                    filename="traced_iq_output.txt"):

        with open(filename, "a") as f:

            f.write(f"\n{'=' * 60}\n")
            f.write(f"{stage_name}\n")
            f.write(f"{'=' * 60}\n")

            for i, sample in enumerate(parameters):

                f.write(f"\nSample {i}\n")

                if isinstance(sample, dict):
                    for key, value in sample.items():
                        f.write(f"{key:<15}: {value}\n")
                else:
                    f.write(f"{sample}\n")
                

    



#---------main-----------
sample_rate = 1000      # 1 kHz it was 2048000
tran = Transmitter (sample_rate)
tran.transmitter()
tran.report()
