import os
import logging
import tkinter as tk
from tkinter import filedialog, messagebox

# Set up logging
logging.basicConfig(
    filename="project_tree_generator.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# List of directories to ignore
IGNORED_DIRS = ['.venv', 'venv', '.git', '__pycache__']

def create_project_tree(root_dir, prefix=""):
    """Recursively scans the directory and builds a tree structure as a string."""
    project_tree = ""

    try:
        entries = os.listdir(root_dir)
        entries.sort()
    except OSError as e:
        logging.error(f"Error accessing directory {root_dir}: {e}")
        return f"Error accessing directory: {root_dir}\n"

    for i, entry in enumerate(entries):
        path = os.path.join(root_dir, entry)
        # Skip ignored directories
        if os.path.isdir(path) and entry in IGNORED_DIRS:
            logging.info(f"Ignoring directory: {path}")
            continue

        connector = "└── " if i == len(entries) - 1 else "├── "
        
        if os.path.isdir(path):
            project_tree += f"{prefix}{connector}{entry}/\n"
            project_tree += create_project_tree(path, prefix + ("    " if i == len(entries) - 1 else "│   "))
        else:
            project_tree += f"{prefix}{connector}{entry}\n"
    
    return project_tree

def scan_python_project(root_dir):
    """Scans a Python project and returns a project tree as a string."""
    try:
        project_name = os.path.basename(os.path.abspath(root_dir))
        project_tree = f"{project_name}/\n"
        project_tree += create_project_tree(root_dir)
    except Exception as e:
        logging.error(f"Error scanning project {root_dir}: {e}")
        return f"Error scanning project: {root_dir}\n"
    
    return project_tree

def save_project_tree_to_file(root_dir, output_file):
    """Saves the project tree to a text file."""
    try:
        project_tree = scan_python_project(root_dir)
        with open(output_file, 'w') as file:
            file.write(project_tree)
        messagebox.showinfo("Success", f"Project tree saved to {output_file}")
        logging.info(f"Project tree successfully saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving project tree: {e}")
        messagebox.showerror("Error", f"Failed to save project tree: {e}")

def select_directory():
    """Open a dialog to select the project directory."""
    try:
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            entry_dir.delete(0, tk.END)  # Clear existing text in entry
            entry_dir.insert(0, folder_selected)
            logging.info(f"Selected directory: {folder_selected}")
    except Exception as e:
        logging.error(f"Error selecting directory: {e}")
        messagebox.showerror("Error", f"Failed to select directory: {e}")

def save_file():
    """Open a dialog to select where to save the text file."""
    project_directory = entry_dir.get()
    
    if not os.path.isdir(project_directory):
        messagebox.showerror("Error", "Please select a valid directory.")
        logging.warning(f"Invalid directory selected: {project_directory}")
        return
    
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save project tree as"
        )
        if file_path:
            save_project_tree_to_file(project_directory, file_path)
    except Exception as e:
        logging.error(f"Error saving file: {e}")
        messagebox.showerror("Error", f"Failed to save file: {e}")

# Set up the main application window
app = tk.Tk()
app.title("Project Tree Generator")
app.geometry("400x150")

# Directory selection section
frame_dir = tk.Frame(app)
frame_dir.pack(pady=10)

label_dir = tk.Label(frame_dir, text="Select Project Directory:")
label_dir.pack(side=tk.LEFT, padx=5)

entry_dir = tk.Entry(frame_dir, width=40)
entry_dir.pack(side=tk.LEFT)

button_browse = tk.Button(frame_dir, text="Browse", command=select_directory)
button_browse.pack(side=tk.LEFT, padx=5)

# Save file button
button_save = tk.Button(app, text="Save Project Tree to File", command=save_file)
button_save.pack(pady=20)

# Start the application loop
app.mainloop()
