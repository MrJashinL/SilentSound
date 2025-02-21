import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import argparse

def find_hidden_patterns(audio_file):
    rate, data = wav.read(audio_file)
    if len(data.shape) == 2:
        data = data.mean(axis=1)
    
    n = len(data)
    k = np.arange(n)
    T = n / rate
    frq = k / T
    frq = frq[range(n // 2)]
    
    Y = fft(data) / n
    Y = Y[range(n // 2)]
    
    plt.plot(frq, abs(Y))
    plt.xlabel('Freq (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Spectrum')
    plt.grid(True)
    plt.show()
    
    threshold = np.max(abs(Y)) * 0.1
    significant_freqs = frq[abs(Y) > threshold]
    
    print("Significant frequencies detected:")
    for freq in significant_freqs:
        print(f"{freq:.2f} Hz")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Identify hidden patterns in musical tones for frequency-based attacks.")
    parser.add_argument("audio", help="Path to the audio file.")
    args = parser.parse_args()
    
    find_hidden_patterns(args.audio)

# Crediti a Jashin L.
