import pandas as pd


filelist = ["file01.txt", "file02.txt", "file03.txt"]

def load_file(filename: str) -> list:
    result = []
    with open(filename) as infile:
        for line in infile.read().splitlines():
            result.append([line])  # Wrap each line in a list to create one column
    return result

# Concatenate the data from all files into a single list
data = []
for filename in filelist:
    data.extend(load_file(filename))

with pd.ExcelWriter("output.xlsx") as writer:
    sheet_name = "combined_data"
    df = pd.DataFrame(data)
    df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
