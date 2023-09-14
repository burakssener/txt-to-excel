import pandas as pd
import glob
import os

folder_path = 'C:/Users/burak/Desktop/instaloader/babybearyuki'  # Replace with your directory path
txt_files = glob.glob(f"{folder_path}/*.txt")

def load_file(filename: str) -> list:
    result = []
    with open(filename, encoding="utf-8") as infile:  # Specify UTF-8 encoding
        for line in infile.read().splitlines():
            result.append([os.path.basename(filename), line])  # Include the file name in each row
    return result

# Concatenate the data from all files into a single list
data = []
for filename in txt_files:
    data.extend(load_file(filename))

with pd.ExcelWriter("output.xlsx") as writer:
    sheet_name = "combined_data"
    df = pd.DataFrame(data, columns=["File Name", "Text"])
    df.to_excel(writer, sheet_name=sheet_name, index=False)
