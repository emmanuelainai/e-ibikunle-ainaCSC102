import pandas as pd

# Create a DataFrame with the company details
data = {
    'Company': ['Enron', 'Anderson', 'GK Jones', 'Mica', 'Dune Industries'],
    'Founded': [1987, 1936, 2001, 1996, 2008],
    'Assets': [1000000, 1500000, 3000000, 250000, None],
    'Liabilities': [200000, 500000, 1500000, 50000, None]
}

df = pd.DataFrame(data)

# Calculate leverage percentage
df['Leverage'] = (df['Assets'] - df['Liabilities']) / df['Assets'] * 100

# Save DataFrame to Excel file
file_name = 'company_details.xlsx'
df.to_excel(file_name, index=False)
print(f"Company details saved to {file_name} successfully.")
