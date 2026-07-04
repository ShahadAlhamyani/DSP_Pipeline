import math
import random

# ChannelSimulator
# │
# ├── inject_doppler()
# ├── inject_isi()
# └── inject_awgn() --------- Done
# └── apply_channel(...)


class Channel:
    def __init__(self, iq_samples):
        self.iq_samples = iq_samples


    def inject_awgn(self,snr_db): # snr_db depened 
        # Signal Power
        noisy_samples = []
        S_power = sum(abs(sample)**2 for sample in self.iq_samples) / len(self.iq_samples)
        snr_linear = 10 ** (snr_db / 10)
        noise_power = S_power / snr_linear
        sigma = math.sqrt(noise_power / 2)
        
        for sample in self.iq_samples :
            noise_I = random.gauss(0, sigma)
            noise_Q = random.gauss(0, sigma)
            noise = complex(noise_I, noise_Q)
            new_sample = sample + noise
            noisy_samples.append(new_sample)
        return noisy_samples






