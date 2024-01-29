import os 

# Directory path where the files are located
folder = r'C:\Users\Andre\Documents\dev\specular_microscopy\assets\images\manual\\'

# Loop to iterate all files contained in the directory
for file_name in os.listdir(folder):
    old_name = folder + file_name # Get the old name
    new_name = folder + 'cropped_' + file_name # Create a new name, *if you want to replace the entire name without keeping any part of the old one, just remove the "file_name"*
    os.rename(old_name, new_name) # Rename the files

print(os.listdir(folder)) # Viewing changes