import pandas as pd

# Load the Excel file
file_path = 'table3.xlsx'
xls = pd.ExcelFile(file_path)

# Load both sheets into dataframes
sheet1 = pd.read_excel(xls, 'table3.csv')
sheet2 = pd.read_excel(xls, 'percentage_difference')

# Function to calculate percentage difference
def calculate_percentage_diff(val1, val2):
    if val1 != 0:
        return ((val2 - val1) / val1) * 100
    return 0

# There are 9 models and each model has 5 inference modes. We will loop over them in groups.
rows_per_model = 5
total_models = 9
num_metrics = 6  # Number of accuracy metrics (columns C to H)

# Loop through the models, comparing performance within the same model's rows
for model_index in range(total_models):
    # Determine the starting row for this model's set of inference modes
    base_row = model_index
    print('base row: ',base_row)
    # Zero-shot row is the first in the group (row 0 of each set)
    zero_shot_row = base_row
    
    # Loop through each of the 4 other inference modes for this model
    for i in range(1, rows_per_model):
        current_row = base_row + i * total_models

        if current_row >= len(sheet1):
            print(f"Skipping row {current_row} as it is out of bounds.")
            continue

        print('current row: ', current_row)
        
        # Calculate percentage difference for each accuracy metric (columns C to H)
        for col_num in range(3, 9):  # Columns C to H
            zero_shot_value = sheet1.iloc[zero_shot_row, col_num - 1]
            print('zero shot value: ', zero_shot_value)
            other_value = sheet1.iloc[current_row, col_num - 1]

            # Calculate percentage difference
            percentage_diff = calculate_percentage_diff(zero_shot_value, other_value)
            
            # Store the result in the corresponding place in sheet2
            sheet2.iloc[current_row - 9, col_num - 1] = percentage_diff

# Save the updated sheet back into an Excel file
output_path = '/Users/hongdong-wan/Documents/Undergraduate Research/updated_table3.xlsx'
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    sheet1.to_excel(writer, sheet_name='table3.csv', index=False)
    sheet2.to_excel(writer, sheet_name='percentage_difference', index=False)

print(f"Updated file saved to: {output_path}")
