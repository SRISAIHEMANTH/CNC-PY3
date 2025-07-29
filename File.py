# file_io_demo.py

import os
from pathlib import Path
from collections import Counter

def count_word_frequencies(input_file, output_file):
    # Check if the input file exists
    if not input_file.exists():
        print(f"Error: The file {input_file} does not exist.")
        return

    # Read the contents of the input file
    with open(input_file, 'r') as file:
        text = file.read().lower()  # Read and convert text to lowercase for case-insensitive counting

    # Split text into words and count frequencies
    words = text.split()
    word_counts = Counter(words)

    # Write the word frequencies to the output file
    with open(output_file, 'w') as file:
        for word, count in word_counts.items():
            file.write(f"{word}: {count}\n")

    print(f"Word frequencies written to {output_file}")

def main():
    # Define file paths using pathlib
    input_path = Path("input.txt")
    output_path = Path("output_word_frequencies.txt")

    # Call the function to count word frequencies
    count_word_frequencies(input_path, output_path)

if __name__ == "__main__":
    main()
