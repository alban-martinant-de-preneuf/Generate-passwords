from itertools import product
import os

def generate_passwords(base_word, prefixes, suffixes):
    variations = []

    for prefix in prefixes:
        for suffix in suffixes:
            variations.append(prefix + base_word + suffix)

    generate_dictionary(variations)

def generate_dictionary(list_of_words):
    folder = "dictionaries"
    filename = input("Enter the name of the file to save the dictionary:\n")

    if not os.path.exists(folder):
        os.makedirs(folder)

    path = folder + "/" + filename

    with open(path, "w") as file:
        for word in list_of_words:
            file.write(word + "\n")

def generate_combinations(elements, lengths):
    if (lengths[0] == ''):
        lengths = [1, len(elements)]
    elif (len(lengths) == 1):
        lengths.insert(0, 1)

    min_length = lengths[0]
    max_length = lengths[1]

    all_combinations = []

    for length in range(int(min_length), int(max_length) + 1):
        # Generate all combinations of given length using itertools.product
        all_combinations += [''.join(combination) for combination in product(elements, repeat=length)]

    return all_combinations

def main():
    base_word = input("Enter a base word:\n")

    prefixes_possible_strings = input("Enter the possible characters or strings that can compose the prefix, separated by commas:\n").replace(" ", "").split(",")
    prefixes_possible_lengths = input("Enter the range of possible repetitions for prefix elements (min, max), separated by a comma:\n").replace(" ", "").split(",")

    suffixes_possible_strings = input("Enter the possible characters or strings that can compose the suffix, separated by commas:\n").replace(" ", "").split(",")
    suffixes_possible_lengths = input("Enter the range of possible repetitions for suffix elements (min, max), separated by a comma:\n").replace(" ", "").split(",")

    # Generate prefix combinations and suffix combinations
    prefixes = generate_combinations(prefixes_possible_strings, prefixes_possible_lengths)
    suffixes = generate_combinations(suffixes_possible_strings, suffixes_possible_lengths)
    
    # Generate and save passwords with variations of prefixes and suffixes
    generate_passwords(base_word, prefixes, suffixes)

# Call the main function to start the program
main()
