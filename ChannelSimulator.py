import math
import random

# ChannelSimulator
# │
# ├── inject_doppler()---------- Done | doppler is fixed for now!
# ├── inject_isi()
# └── inject_awgn() ------------ Done
# └── apply_channel(...)


class Channel:
    def __init__(self, iq_samples):
        self.iq_samples = iq_samples

    def inject_doppler(self, sample_rate = 20000, doppler_hz=100):
        doppler_rotated_samples = []
        doppler_packet = []
        for n, sample in enumerate(self.iq_samples) :
            phase = (2*math.pi*doppler_hz) * n/sample_rate
            rotation = complex(math.cos(phase), math.sin(phase))
            new_sample = sample * rotation
            doppler_rotated_samples.append(new_sample) 

            doppler_packet.append({ # temporary | for trace purpose only
                "stage": "inject_doppler",
                "n":n,
                "phase":phase,
                "rotation":rotation,
                "new_sample":new_sample,
            })

        return { "doppler_rotated_samples":doppler_rotated_samples,
                "doppler_packet":doppler_packet}


    def inject_awgn(self,snr_db): # snr_db depened 
        
        inject_awgn_packet = []
        noisy_samples = []
        result = self.inject_doppler()
        doppler_samples = result["doppler_rotated_samples"]

        S_power = sum(abs(sample)**2 for sample in doppler_samples) / len(doppler_samples)
        snr_linear = 10 ** (snr_db / 10)
        noise_power = S_power / snr_linear
        sigma = math.sqrt(noise_power / 2)
        
        for n, sample in enumerate(doppler_samples):
            noise_I = random.gauss(0, sigma)
            noise_Q = random.gauss(0, sigma)
            noise = complex(noise_I, noise_Q)
            new_sample = sample + noise
            noisy_samples.append(new_sample)

            inject_awgn_packet.append({ # temporary | for trace purpose only
            "stage": "inject_awgn",
            "n":n,
            "S_power": S_power,
            "snr_linear": snr_linear,
            "noise_power": noise_power,
            "sigma":sigma,
            "noise_I":noise_I,
            "noise_Q":noise_Q,
            "new_sample":new_sample,
        })   

        return {"noisy_samples":noisy_samples,
                "inject_awgn_packet":inject_awgn_packet}

    




