import pandas as pd
import glob
import os

folder_path = 'C:/Users/burak/Desktop/instaloader/babybearyuki'  # Replace with your directory path
txt_files = glob.glob(f"{folder_path}/*.txt")

def load_file(filename: str) -> list:
    result = []
    file_texts = []  # Store text lines for each file
    with open(filename, encoding="utf-8") as infile:
        for line in infile.read().splitlines():
            if line.strip():  # Check if the line is not empty
                file_texts.append(line)  # Collect non-empty lines
    result.append([os.path.basename(filename), "\n".join(file_texts)])  # Include the file name and combined text
    return result

# Concatenate the data from all files into a single list
data = []
for filename in txt_files:
    data.extend(load_file(filename))

with pd.ExcelWriter("output.xlsx") as writer:
    sheet_name = "combined_data"
    df = pd.DataFrame(data, columns=["File Name", "Text"])
    df.to_excel(writer, sheet_name=sheet_name, index=False)
