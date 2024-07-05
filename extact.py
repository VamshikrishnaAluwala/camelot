import camelot
import pandas as pd

# Read all tables from the PDF file
pdf_file = '/Users/vamshi/Documents/GenAI/camelot/camelot.pdf'
print(f"Reading tables from PDF file: {pdf_file}")
tables = camelot.read_pdf(pdf_file, pages='all')
print(f"Found {len(tables)} tables in the PDF file.")

# Concatenate all tables into a single DataFrame
all_tables_df = pd.concat([table.df for table in tables])

# Export the combined DataFrame to a single CSV file
all_tables_df.to_csv('finaldata.csv', index=False)
print("Exported all tables to finaldata.csv")
