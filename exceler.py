import pandas as pd
import glob

folder_path = 'C:/Users/burak/Desktop/exceler/'
txt_files = glob.glob(f"{folder_path}/*.txt")

def load_file(filename: str) -> list:
    result = []
    with open(filename, encoding='utf-8') as infile:
        for line in infile.read().splitlines():
            result.append(line.split())
    return result

# Create a dummy DataFrame for the first sheet
dummy_df = pd.DataFrame(["Dummy"])
sheet_names = ["sheet1", "sheet2", "sheet3"]

with pd.ExcelWriter("output.xlsx") as writer:
    # Save the dummy DataFrame to the first sheet
    dummy_df.to_excel(writer, sheet_name=sheet_names[0], index=False, header=False)

    # Iterate through the rest of the files and create new sheets
    for idx, filename in enumerate(txt_files):
        df = pd.DataFrame(load_file(filename))
        # Save the data to subsequent sheets
        df.to_excel(writer, sheet_name=sheet_names[idx + 1], index=False, header=False)
