import math
import struct



def analyzer(iq_samples, sample_rate):    
    prev_theta = 0
    signal =[]
    analyzer_packet =[]

    for n, sample in enumerate(iq_samples):

        
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

        analyzer_packet.append({
            "n":n,    # temporary | for trace purpose only
            "I":I,
            "Q":Q,
            "amplitude":amplitude,
            "theta":theta,
            "theta_deg":theta_deg,
            "prev_theta":prev_theta,
            "delta_theta":delta_theta,
            "frequency":frequency,
        })        

    write_file(signal)  

    return  analyzer_packet




def write_file(data, filename = "iq_output_final_result.txt"):
    with open(filename,"w") as f:
        sample_len = 0
        for sample in data:
            sample_len +=1
            f.write(
                f"smaple number = {sample_len}, "
                f"Amplitude ={sample['Amplitude']:.3f}, "
                f"Theta ={sample['Theta']:.3f}, "
                f"Delta Theta ={sample['delta']:.3f}, "
                f"Frequency ={sample['Frequency']:.3f}Hz \n"
            )

    return filename
