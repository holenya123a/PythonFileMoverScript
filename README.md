
### Optional arguments:
- `-h`, `--help`: Show this help message and exit.
- `-p PATH`, `--path PATH`: Path to the designated directory.

## Features
- Detects duplicate files within a directory.
- Provides options to move or delete duplicate files.
- Supports customization through command-line arguments.

## Command-line Options
- `-p PATH`, `--path PATH`: Specifies the path to the directory containing the files to be analyzed.

## Installation
1. Clone the repository from GitHub.
2. Install Poetry.
3. Navigate to the directory containing the script.
4. Execute command poetry init.
5. Execute the script using Python.

## Examples
1. To detect duplicates in a specific directory:
poetry run python __main__.py -p /path/to/directory

2. To run the script without specifying a directory (uses environment variable DIR_PATH if defined):

## Usage Instructions
1. Run the script from the command line.
2. If no path is specified, ensure that the environment variable `DIR_PATH` is defined.
3. Follow the on-screen instructions to choose whether to move or delete duplicate files.

## Dependencies
- Python 3.x
- `argparse` module
- `os` module
- `file_manager` module
- `print_options` module
- `poetry` module

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
