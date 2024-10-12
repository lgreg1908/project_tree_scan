
# Project Tree Generator

## Overview

**Project Tree Generator** is a Python-based utility that allows users to generate a hierarchical tree structure of a Python project directory, while ignoring certain directories such as `.venv`, `venv`, `.git`, and `__pycache__`. The tool comes with a simple graphical user interface (GUI) built using `tkinter`, making it easy to browse, select directories, and save the project tree to a text file.

The project can also be compiled into a standalone executable using PyInstaller, allowing users to run it without having Python installed.

## Features

- Generate a tree structure of a Python project directory.
- Ignore unnecessary directories like `.venv`, `.git`, and `__pycache__`.
- Simple GUI for browsing directories and saving the tree to a text file.
- Logs all actions and errors for easier troubleshooting.
- Cross-platform support (Windows, macOS, Linux).

## Installation & Usage

### Option 1: Running the Python Script

1. **Install dependencies**:
   
   Make sure you have Python installed. Install the required packages by running:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, install `tkinter` if it's not pre-installed on your system:

   ```bash
   pip install python-tk
   ```

2. **Run the script**:

   ```bash
   python project_tree_generator.py
   ```

3. **Usage**:

   - Browse to the project directory you want to scan.
   - Save the project tree as a text file.

### Option 2: Running the Standalone Executable

If you don't want to install Python, you can use the standalone executable that was built using PyInstaller.

1. **Download the executable** (for Windows/macOS/Linux) from the release section or build it yourself using the instructions below.
2. Run the executable, and the graphical user interface (GUI) will open.
3. Browse for the project directory, and click **Save Project Tree to File** to generate the tree.

> **Note**: The standalone executable does not require Python to be installed on the user's machine.

## Building the Executable

If you want to build the standalone executable yourself, follow these steps:

1. **Install PyInstaller**:

   Install `PyInstaller` using pip:

   ```bash
   pip install pyinstaller
   ```

2. **Create the executable**:

   Run the following command to package the script into a standalone executable:

   ```bash
   pyinstaller --onefile --windowed project_tree_generator.py
   ```

3. **Find the executable**:

   Once the process is complete, you'll find the standalone executable in the `dist/` directory.

## Directory Ignored by the Tool

By default, the following directories are ignored by the tool to keep the project tree clean:

- `.venv`
- `venv`
- `.git`
- `__pycache__`

You can easily modify the script to add more directories to this list by editing the `IGNORED_DIRS` list in the code.

## Logging

The tool generates a log file `project_tree_generator.log` that records actions, errors, and ignored directories for easy debugging and auditing.

## Example Project Tree Output

For example, if you have a project directory like this:

```
my_project/
├── .venv/
├── .git/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
└── README.md
```

The generated project tree would look like this (excluding `.venv` and `.git`):

```
my_project/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
└── README.md
```

## Contributing

Feel free to fork this project, make improvements, and submit pull requests. We welcome all kinds of contributions including:
- Adding new features.
- Fixing bugs.
- Improving documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
