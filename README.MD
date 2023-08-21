# Password Generator

This Python script generates passwords by combining a base word with various prefixes and suffixes. It creates a dictionary of possible passwords based on the specified inputs.


## Getting Started

1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Run the script by executing `python generatPwdsFromBase.py`.
4. Follow the prompts to provide a base word, possible characters/strings for prefixes, possible lengths of prefixes, possible characters/strings for suffixes, and possible lengths of suffixes.
5. The script will generate variations of passwords using different combinations of prefixes and suffixes and save them to a file.


## Example

Here's an example of how to use the program:

1. Enter a base word:
`pass`
2. Enter possible characters or strings that can compose the prefix, separated by commas:
`pre,ex`
3. Enter the range of possible repetitions for prefix elements (min, max), separated by a comma:
`1,1`
4. Enter possible characters or strings that can compose the suffix, separated by commas:
`123,!`
5. Enter the range of possible repetitions for suffix elements (min, max), separated by a comma:
`2,3`
6. Enter the name of the file to save the dictionary:
`dictionary.txt`
7. The content of `dictionary.txt` will be :
```text
prepass123123
prepass123!
prepass!123
prepass!!
prepass123123123
prepass123123!
prepass123!123
prepass123!!
prepass!123123
prepass!123!
prepass!!123
prepass!!!
expass123123
expass123!
expass!123
expass!!
expass123123123
expass123123!
expass123!123
expass123!!
expass!123123
expass!123!
expass!!123
expass!!!
```

## Contributions

Contributions and suggestions are welcome! If you find a bug or have an improvement idea, please create an issue or a pull request.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
