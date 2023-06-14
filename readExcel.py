import pandas as pd

def readExcelFile(path):
# Read the Excel sheet into a DataFrame
    df = pd.read_excel(path)

    # Create an empty dictionary to store the data
    data = {}

    # Iterate over the rows of the DataFrame
    for row in df.values:
        # Get the value from the first column (e.g., 200, 300, etc.)
        value = row[0]
        # Create an inner dictionary for the values in the remaining columns
        inner_dict = {}
        # Iterate over the remaining columns and populate the inner dictionary
        for i, col in enumerate(df.columns[1:]):
            inner_dict[i + 1 + value*100] = row[i + 1]
        # Add the inner dictionary to the main dictionary
        data[value] = inner_dict

    # Print the resulting dictionary
    return data