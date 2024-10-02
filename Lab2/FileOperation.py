def count_vowels(text):
    """Count the number of vowels in the given text."""
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)


def process_file(input_file, output_file):
    """Read from input_file, count vowels in each line, and write results to output_file."""
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line_number, line in enumerate(infile, start=1):
                # Count vowels in the current line
                vowel_count = count_vowels(line)
                result = f"Line {line_number}: {vowel_count} vowels"

                # Write the result to the output file
                outfile.write(result + '\n')

                # Print the result to the console
                print(result)

        print("Processing complete. Results written to output.txt.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IOError as e:
        print(f"Error: {e}")


# Specify the input and output file names
input_filename = 'input.txt'
output_filename = 'output.txt'

# Process the file
process_file(input_filename, output_filename)
