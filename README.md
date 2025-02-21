# Silent Sound

Creato da Jashin L.

Questa raccolta include vari strumenti progettati per manipolare file audio, sfruttare vulnerabilità nei codec audio e nei player, e creare pagine di phishing. Ogni strumento è descritto in dettaglio con istruzioni su come utilizzarlo.

## Strumenti Inclusi

1. [MIDIInjection](#midiinjection)
2. [KeyFinder](#keyfinder)
3. [JeeHyu](#jeehyu)
4. [NoiseInjection](#noiseinjection)
5. [MP3Exploit](#mp3exploit)
6. [SpotifyPhish](#spotifyphish)

---

## MIDIInjection

### Descrizione

Modifica file MIDI per iniettare comandi nascosti in tracce musicali.

### Implementazione

Il tool è implementato in C#.

### Utilizzo

1. Compila il file `MIDIInjection.cs` utilizzando un compilatore C#.
2. Esegui il tool con i seguenti comandi:

Per iniettare dati:
```sh
dotnet run inject <midi_file> <output_file> <data>
```

Per estrarre dati:
```sh
dotnet run extract <midi_file>
```

---

## KeyFinder

### Descrizione

Identifica pattern nascosti nei toni musicali per attacchi basati su frequenze.

### Implementazione

Il tool è implementato in Python.

### Utilizzo

1. Assicurati di avere `numpy` e `scipy` installati sul tuo sistema.
2. Esegui il tool con il comando:

```sh
python KeyFinder.py <audio_file>
```

---

## JeeHyu

### Descrizione

Sfrutta vulnerabilità nei codec audio per exploit buffer overflow.

### Implementazione

Il tool è implementato in due parti: Python per generare il file WAV con il payload malevolo e C per eseguire l'exploit.

### Utilizzo

1. Genera il file WAV con il payload:
```sh
python JeeHyuGenerator.py exploit.wav "your_payload_here"
```

2. Compila ed esegui il file C:
```sh
gcc -o JeeHyuExploit JeeHyuExploit.c
./JeeHyuExploit exploit.wav
```

---

## NoiseInjection

### Descrizione

Aggiunge impercettibili variazioni sonore per alterare l'output di AI e modelli di riconoscimento vocale.

### Implementazione

Il tool è implementato in Python.

### Utilizzo

1. Assicurati di avere `numpy` e `scipy` installati sul tuo sistema.
2. Esegui il tool con il comando:

```sh
python NoiseInjection.py <input_file> <output_file> --noise_level <noise_level>
```

---

## MP3Exploit

### Descrizione

Crea file MP3 contenenti codice malevolo sfruttando vulnerabilità nei player audio.

### Implementazione

Il tool è implementato in due parti: Python per generare il file MP3 con il payload malevolo e C per eseguire l'exploit.

### Utilizzo

1. Genera il file MP3 con il payload:
```sh
python MP3ExploitGenerator.py exploit.mp3 "your_payload_prefix;your_malicious_command_here"
```

2. Compila ed esegui il file C:
```sh
gcc -o MP3Exploit MP3Exploit.c
./MP3Exploit exploit.mp3
```

---

## SpotifyPhish

### Descrizione

Strumento per il phishing via playlist Spotify contraffatte.

### Implementazione

Il tool è implementato in HTML, CSS, JavaScript e Python.

### Utilizzo

1. Assicurati di avere Flask installato sul tuo sistema. Puoi installarlo utilizzando `pip`:
```sh
pip install flask
```

2. Avvia il server Python:
```sh
python server.py
```

3. Apri il file `spotify_phish.html` nel tuo browser per visualizzare la pagina di phishing.

---

Assicurati di utilizzare questi tool in un ambiente controllato e solo a scopo di ricerca. Ogni strumento è stato creato per scopi educativi e di ricerca sulla sicurezza informatica.

