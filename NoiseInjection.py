import numpy as np
import scipy.io.wavfile as wav
import argparse

def add_noise(input_file, output_file, noise_level=0.005):
    # Read the input WAV file
    rate, data = wav.read(input_file)
    
    # Normalize data if it's stereo
    if len(data.shape) == 2:
        data = data.mean(axis=1)
    
    # Generate white noise
    noise = np.random.normal(0, noise_level, data.shape)
    
    # Add noise to the original audio signal
    noisy_data = data + noise
    
    # Ensure the noisy data is within the valid range
    noisy_data = np.clip(noisy_data, -32768, 32767)
    
    # Convert back to int16
    noisy_data = noisy_data.astype(np.int16)
    
    # Write the noisy audio to a new WAV file
    wav.write(output_file, rate, noisy_data)
    
    print(f"Noisy audio file created: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add imperceptible noise to audio files to alter the output of AI and speech recognition models.")
    parser.add_argument("input", help="Path to the input WAV file.")
    parser.add_argument("output", help="Path to the output WAV file.")
    parser.add_argument("--noise_level", type=float, default=0.005, help="Level of noise to add (default: 0.005)")
    args = parser.parse_args()
    
    add_noise(args.input, args.output, args.noise_level)

# Crediti a Jashin L.
