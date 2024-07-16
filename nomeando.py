import os
import random
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter window
root = tk.Tk()
root.withdraw()

# Prompt the user to select a directory
directory = filedialog.askdirectory()

# Get a list of all files in the selected directory
files = os.listdir(directory)

# Iterate over each file and rename it randomly
for file in files:
    # Generate a random name
    random_name = ''.join(random.choices('123456789', k=3))

    # Get the file extension
    file_extension = os.path.splitext(file)[1]

    # Construct the new file name with the random name and original extension
    new_file_name = random_name + file_extension

    # Rename the file
    os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))

print("Files renamed successfully!")