import pandas as pd

# Load the CSV files
df_alpha = pd.read_csv('new_test_alphabet.csv')
df_num = pd.read_csv('new_test_numeric.csv')

# Merge the DataFrames on common columns
merged_df = pd.merge(df_alpha, df_num, on=['frame_nmr', 'car_id'], how='outer', suffixes=('_alpha', '_num'))

def combine_bbox(alpha_bbox, num_bbox):
    """
    Combine bounding boxes from two sources by ensuring they are not duplicated.
    """
    if pd.notna(alpha_bbox) and pd.notna(num_bbox):
        # Assuming bbox format is consistent and just need to be combined without duplication
        return alpha_bbox.split('[')[0] + '[' + num_bbox.split('[')[-1]
    elif pd.notna(alpha_bbox):
        return alpha_bbox
    elif pd.notna(num_bbox):
        return num_bbox
    return ''

def combine_score(alpha_score, num_score):
    """
    Combine scores from two sources by ensuring they are not duplicated.
    """
    alpha_score = str(alpha_score) if pd.notna(alpha_score) else ''
    num_score = str(num_score) if pd.notna(num_score) else ''
    if alpha_score and num_score:
        # Avoid duplication of scores
        return alpha_score.split('.')[0] + '.' + num_score.split('.')[-1]
    elif alpha_score:
        return alpha_score
    elif num_score:
        return num_score
    return ''

def combine_license_number(alpha_number, num_number):
    """
    Combine license numbers from two sources by concatenating them and ensuring correct formatting.
    """
    alpha_number = str(alpha_number) if pd.notna(alpha_number) else ''
    num_number = str(num_number) if pd.notna(num_number) else ''
    if alpha_number and num_number:
        return alpha_number + num_number
    elif alpha_number:
        return alpha_number
    elif num_number:
        return num_number
    return ''

# List of columns to combine
columns_to_combine = {
    'car_bbox': ('car_bbox_alpha', 'car_bbox_num'),
    'license_plate_bbox': ('license_plate_bbox_alpha', 'license_plate_bbox_num'),
    'license_plate_bbox_score': ('license_plate_bbox_score_alpha', 'license_plate_bbox_score_num'),
    'license_number': ('license_number_alpha', 'license_number_num'),
    'license_number_score': ('license_number_score_alpha', 'license_number_score_num')
}

# Apply the combination functions to each column
for final_col, (alpha_col, num_col) in columns_to_combine.items():
    if final_col == 'car_bbox' or final_col == 'license_plate_bbox':
        merged_df[final_col] = merged_df.apply(lambda row: combine_bbox(row.get(alpha_col, ''), row.get(num_col, '')), axis=1)
    elif final_col == 'license_plate_bbox_score' or final_col == 'license_number_score':
        merged_df[final_col] = merged_df.apply(lambda row: combine_score(row.get(alpha_col, ''), row.get(num_col, '')), axis=1)
    elif final_col == 'license_number':
        merged_df[final_col] = merged_df.apply(lambda row: combine_license_number(row.get(alpha_col, ''), row.get(num_col, '')), axis=1)

# Drop the original separate columns
columns_to_drop = [col for sublist in columns_to_combine.values() for col in sublist]
merged_df.drop(columns=columns_to_drop, inplace=True)

# Fill NaN values with empty strings
merged_df.fillna('', inplace=True)

# Save the result to a new CSV file
merged_df.to_csv('merged_license_plate_info.csv', index=False)

print("Cleaned and merged CSV file has been created successfully.")
