import pandas as pd
import sys

def clean_data(input1, input2, output):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)

    # 1. Merge the two input data files based on the ID value
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')

    # 2. Drop rows with missing values
    merged_df.dropna(inplace=True)

    # 3. Drop rows where the job value contains 'insurance' or 'Insurance'
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

    # 4. Remove the redundant 'id' column from the merged dataframe
    merged_df.drop('id', axis=1, inplace=True)

    # 5. Save the cleaned data to the specified output file
    merged_df.to_csv(output, index=False)

    print("Data cleaning completed. Cleaned data saved to", output)

if __name__ == "__main__":
    input1 = 'respondent_contact.csv'
    input2 = 'respondent_other.csv'
    output = 'respondent_cleaned.csv'

    clean_data(input1, input2, output)