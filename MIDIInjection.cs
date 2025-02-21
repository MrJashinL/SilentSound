using System;
using System.IO;
using NAudio.Midi;

namespace MIDIInjection
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length < 3)
            {
                Console.WriteLine("Usage: MIDIInjection <mode> <midi_file> <output_file> [<data>]");
                Console.WriteLine("Modes: inject, extract");
                return;
            }

            string mode = args[0];
            string midiFilePath = args[1];
            string outputFilePath = args[2];

            if (mode.Equals("inject", StringComparison.OrdinalIgnoreCase))
            {
                if (args.Length < 4)
                {
                    Console.WriteLine("Data to inject is required for inject mode.");
                    return;
                }
                string data = args[3];
                InjectData(midiFilePath, outputFilePath, data);
            }
            else if (mode.Equals("extract", StringComparison.OrdinalIgnoreCase))
            {
                ExtractData(midiFilePath);
            }
            else
            {
                Console.WriteLine("Invalid mode. Supported modes: inject, extract");
            }
        }

        static void InjectData(string midiFilePath, string outputFilePath, string data)
        {
            var midiFile = new MidiFile(midiFilePath, false);
            var metaEvent = new TextEvent(data, MetaEventType.SequenceTrackName, 0);
            midiFile.Events[0].Insert(0, metaEvent);
            midiFile.Save(outputFilePath);
            Console.WriteLine($"Data injected into {outputFilePath}");
        }

        static void ExtractData(string midiFilePath)
        {
            var midiFile = new MidiFile(midiFilePath, false);
            foreach (var track in midiFile.Events)
            {
                foreach (var midiEvent in track)
                {
                    if (midiEvent is TextEvent textEvent && textEvent.MetaEventType == MetaEventType.SequenceTrackName)
                    {
                        Console.WriteLine($"Extracted data: {textEvent.Text}");
                        return;
                    }
                }
            }
            Console.WriteLine("No hidden data found in the MIDI file.");
        }
    }

    // Crediti a Jashin L.
}
