import pandas as pd
from numpy import NaN

# the Sentence Date and Custody Date columns can either be in the form MMDDYYYY.0 (a float) or "YYYY-MM-DD 00:00:00" (a string). We want to make them all in the second form
def convert_float_to_datetime(value):
    if isinstance(value, float):
        date_str = str(int(value))
        return f"{date_str[-4:]}-{date_str[:2]}-{date_str[2:4]} 00:00:00"
    return value

df = pd.read_csv("/Users/kacpermocarski/Desktop/New_CSVs/combined_data.csv")
# limit columns to only the necessary ones
df = df[['IDOC #', 'Name', 'Date of Birth', 'Sex', 'Race', 'Veteran Status', 'Current Admission Date', 'Admission Type', 'Parent Institution', 'Projected Mandatory Supervised Release (MSR) Date3', 'Projected Discharge Date3', 'Custody Date', 'Sentence Date', 'Crime Class', 'Holding Offense', 'Sentence Years', 'Sentence Months', 'Truth in Sentencing', 'Sentencing County']]
# drop the unncessary rows (they aren't names, they are other pieces of data)
df = df[df['Name'].notna()]
df = df[df["Sentence Date"].notna()]

# changing from MMDDYYYY.0 format (float) to "YYYY-MM-DD 00:00:00" format (string)
df['Sentence Date'] = df['Sentence Date'].apply(convert_float_to_datetime)
df['Custody Date'] = df['Sentence Date'].apply(convert_float_to_datetime)

df.to_csv("/Users/kacpermocarski/Desktop/New_CSVs/combined_data.csv", index=False)