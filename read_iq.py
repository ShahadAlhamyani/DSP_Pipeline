import struct

def read_iq(filename):
    samples = []

    with open(filename, "rb") as f:
        while True:
            data = f.read(8)

            if len(data) < 8:
                break

            I, Q = struct.unpack("ff", data)
            samples.append(complex(I, Q))

    return samples