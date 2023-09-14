import pandas as pd
import os

# Define the parent directory containing subdirectories with text files
parent_directory = 'C:/Users/burak/Desktop/instaloader'

# Initialize an empty list to store data
data = []

# Iterate through subdirectories and their files using os.walk
for root, dirs, files in os.walk(parent_directory):
    for file in files:
        if file.endswith(".txt"):  # Check if the file has a .txt extension
            file_path = os.path.join(root, file)  # Get the full file path
            with open(file_path, encoding="utf-8") as infile:
                text = infile.read()
                data.append([file, text])

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=["File Name", "Text"])

# Save the data to an Excel file
with pd.ExcelWriter("output.xlsx") as writer:
    sheet_name = "combined_data"
    df.to_excel(writer, sheet_name=sheet_name, index=False)