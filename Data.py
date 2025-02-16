import re
import pandas as pd

def markdown_to_csv(llm_output):
    
    # Find all Markdown tables
    tables = re.findall(r"(\|(?:[^\n]+\|)+\n\|(?:\s*-+\s*\|)+\n(?:\|(?:[^\n]+\|)+\n)+)", llm_output)
    
    dataframes = []
    
    for table in tables:
        # Split lines and extract columns
        lines = table.strip().split("\n")
        headers = [col.strip() for col in lines[0].split("|")[1:-1]]  # Headers
        data_rows = [line.split("|")[1:-1] for line in lines[2:]]  # Ignore separator row

        # Clean and validate rows
        cleaned_data = [ [col.strip() for col in row] for row in data_rows if len(row) == len(headers)]

        if cleaned_data:
            df = pd.DataFrame(cleaned_data, columns=headers)
            dataframes.append(df)
        return dataframes