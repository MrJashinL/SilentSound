import wave
import argparse

def hide_data(audio_file, output_file, data):
    audio = wave.open(audio_file, 'rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    data = data + int((len(frame_bytes)-(len(data)*8*8))/8) * '#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in data])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)
    with wave.open(output_file, 'wb') as fd:
        fd.setparams(audio.getparams())
        fd.writeframes(frame_modified)
    audio.close()
    print(f"Data hidden in {output_file}")

def retrieve_data(audio_file):
    audio = wave.open(audio_file, 'rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    data = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0, len(extracted), 8))
    decoded = data.split("###")[0]
    audio.close()
    print(f"Data retrieved: {decoded}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hide or retrieve data in audio files using steganography.")
    parser.add_argument("mode", choices=["hide", "retrieve"], help="Mode of operation: 'hide' to hide data, 'retrieve' to retrieve data.")
    parser.add_argument("--audio", required=True, help="Path to the audio file.")
    parser.add_argument("--output", help="Path to the output file (required for 'hide' mode).")
    parser.add_argument("--data", help="Data to hide (required for 'hide' mode).")
    
    args = parser.parse_args()
    
    if args.mode == "hide":
        if not args.output or not args.data:
            parser.error("Output file and data are required for 'hide' mode.")
        else:
            hide_data(args.audio, args.output, args.data)
    elif args.mode == "retrieve":
        retrieve_data(args.audio)

# Crediti a Jashin L.
