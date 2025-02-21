package main

import (
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/dhowden/tag"
	"github.com/mikkyang/id3-go"
	"github.com/mikkyang/id3-go/v2"
)

func extractMetadata(audioFilePath string) {
	file, err := os.Open(audioFilePath)
	if err != nil {
		log.Fatalf("Failed to open audio file: %v", err)
	}
	defer file.Close()

	if strings.HasSuffix(strings.ToLower(audioFilePath), ".mp3") {
		extractID3Metadata(file)
	} else if strings.HasSuffix(strings.ToLower(audioFilePath), ".wav") {
		extractTagMetadata(file)
	} else {
		fmt.Println("Unsupported audio file format. Supported formats are: .mp3, .wav")
	}
}

func extractID3Metadata(file *os.File) {
	tag, err := id3v2.Parse(file)
	if err != nil {
		log.Fatalf("Failed to read ID3 metadata from audio file: %v", err)
	}

	fmt.Printf("Title: %s\n", tag.Title())
	fmt.Printf("Artist: %s\n", tag.Artist())
	fmt.Printf("Album: %s\n", tag.Album())
	fmt.Printf("Genre: %s\n", tag.Genre())
	fmt.Printf("Year: %s\n", tag.Year())
}

func extractTagMetadata(file *os.File) {
	metadata, err := tag.ReadFrom(file)
	if err != nil {
		log.Fatalf("Failed to read metadata from audio file: %v", err)
	}

	fmt.Printf("Title: %s\n", metadata.Title())
	fmt.Printf("Artist: %s\n", metadata.Artist())
	fmt.Printf("Album: %s\n", metadata.Album())
	fmt.Printf("Genre: %s\n", metadata.Genre())
	fmt.Printf("Year: %d\n", metadata.Year())
	fmt.Printf("Comment: %s\n", metadata.Comment())
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run echospy.go <audio_file>")
		return
	}

	audioFilePath := os.Args[1]
	extractMetadata(audioFilePath)
}

// Crediti a Jashin L.
