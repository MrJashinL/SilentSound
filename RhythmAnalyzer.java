import javax.sound.sampled.*;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;

public class RhythmAnalyzer {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java RhythmAnalyzer <mode> <audio_file>");
            System.out.println("Modes: analyze");
            return;
        }

        String mode = args[0];
        String audioFilePath = args[1];

        if ("analyze".equalsIgnoreCase(mode)) {
            try {
                analyzeAudioFile(audioFilePath);
            } catch (Exception e) {
                System.err.println("Error analyzing audio file: " + e.getMessage());
            }
        } else {
            System.out.println("Invalid mode. Supported mode: analyze");
        }
    }

    private static void analyzeAudioFile(String filePath) throws UnsupportedAudioFileException, IOException {
        File audioFile = new File(filePath);
        AudioInputStream audioStream = AudioSystem.getAudioInputStream(audioFile);
        AudioFormat format = audioStream.getFormat();
        long frames = audioStream.getFrameLength();
        double durationInSeconds = (frames + 0.0) / format.getFrameRate();

        byte[] audioBytes = new byte[(int) (frames * format.getFrameSize())];
        audioStream.read(audioBytes);

        double[] audioData = new double[audioBytes.length / 2];
        for (int i = 0; i < audioData.length; i++) {
            audioData[i] = ((audioBytes[2 * i + 1] << 8) | audioBytes[2 * i] & 0xFF) / 32768.0;
        }

        double[][] spectrogram = computeSpectrogram(audioData, format.getSampleRate());

        analyzeSpectrogram(spectrogram, durationInSeconds);

        audioStream.close();
    }

    private static double[][] computeSpectrogram(double[] audioData, float sampleRate) {
        int windowSize = 1024;
        int overlap = windowSize / 2;
        int steps = (audioData.length - windowSize) / overlap;

        double[][] spectrogram = new double[steps][windowSize / 2];
        for (int i = 0; i < steps; i++) {
            double[] window = Arrays.copyOfRange(audioData, i * overlap, i * overlap + windowSize);
            double[] spectrum = computeFFT(window);
            System.arraycopy(spectrum, 0, spectrogram[i], 0, spectrum.length);
        }

        return spectrogram;
    }

    private static double[] computeFFT(double[] window) {
        int n = window.length;
        double[] spectrum = new double[n / 2];
        double[] real = new double[n];
        double[] imag = new double[n];

        for (int i = 0; i < n; i++) {
            real[i] = window[i];
            imag[i] = 0;
        }

        for (int i = 0; i < n; i++) {
            int j = Integer.reverse(i) >>> (32 - Integer.numberOfTrailingZeros(n));
            if (i < j) {
                double tempReal = real[i];
                double tempImag = imag[i];
                real[i] = real[j];
                imag[i] = imag[j];
                real[j] = tempReal;
                imag[j] = tempImag;
            }
        }

        for (int len = 2; len <= n; len <<= 1) {
            double angle = -2 * Math.PI / len;
            double wReal = Math.cos(angle);
            double wImag = Math.sin(angle);

            for (int i = 0; i < n; i += len) {
                double uReal = 1;
                double uImag = 0;
                for (int j = 0; j < len / 2; j++) {
                    int evenIndex = i + j;
                    int oddIndex = i + j + len / 2;
                    double tReal = uReal * real[oddIndex] - uImag * imag[oddIndex];
                    double tImag = uReal * imag[oddIndex] + uImag * real[oddIndex];

                    real[oddIndex] = real[evenIndex] - tReal;
                    imag[oddIndex] = imag[evenIndex] - tImag;
                    real[evenIndex] += tReal;
                    imag[evenIndex] += tImag;

                    double tempReal = uReal;
                    uReal = tempReal * wReal - uImag * wImag;
                    uImag = tempReal * wImag + uImag * wReal;
                }
            }
        }

        for (int i = 0; i < n / 2; i++) {
            spectrum[i] = Math.sqrt(real[i] * real[i] + imag[i] * imag[i]);
        }

        return spectrum;
    }

    private static void analyzeSpectrogram(double[][] spectrogram, double duration) {
        for (int i = 0; i < spectrogram.length; i++) {
            for (int j = 0; j < spectrogram[i].length; j++) {
                if (spectrogram[i][j] > 0.5) {
                    System.out.println("Potential hidden message detected at time " + (i * 0.5) + "s");
                }
            }
        }
    }

    // Crediti a Jashin L.
}
