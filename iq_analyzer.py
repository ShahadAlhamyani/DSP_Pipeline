import math
import struct

# the generated signals will be noiseless (Ideal Signal) 

def analyzer(iq_samples, sample_rate):    
    prev_theta = 0
    signal =[]

    for sample in iq_samples:

        
        I = sample.real
        Q = sample.imag
                
        amplitude = math.sqrt(I**2 + Q**2)
        theta = math.atan2(Q,I)
        theta_deg = math.degrees(theta)
        
        delta_theta =  theta_deg - prev_theta
        prev_theta = theta_deg

        # unwrapping
        if delta_theta < -180 :
            delta_theta = delta_theta + 360
        elif delta_theta > 180 :
            delta_theta = delta_theta - 360  

        frequency = (delta_theta / 360) * sample_rate  

        signal.append({
            "Amplitude": amplitude,
            "Theta": theta,
            "delta": delta_theta,
            "Frequency": frequency
        })

        write_file(signal)    


#|||||||||||**لازم اطبع عداد عشان احسب بعض العينات يدوياً واتاكد منها**|||||||||||

def write_file(data, filename = "iq_output.txt"):
    with open(filename,"w") as f:
        for sample in data:

            f.write(
                f"Amplitude={sample['Amplitude']:.3f}, "
                f"Theta={sample['Theta']:.3f}, "
                f"Delta Theta={sample['delta']:.3f}, "
                f"Frequency={sample['Frequency']:.3f}Hz\n"
            )

    return filename
