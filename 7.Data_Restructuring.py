import pandas as pd
import os
import re
from io import StringIO  # <- important if reading CSV from a string

# Creating the backtesting directory
output_dir = "backtesting"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Reading the CSV data into a DataFrame
# If reading from a string:
# df = pd.read_csv(StringIO(data), index_col=0)

# If reading from a file:
df = pd.read_csv("output.csv", index_col=0)

# Function to clean and format values
def format_value(value):
    if pd.isna(value):
        return "N/A"
    try:
        value = float(value)
        if value == float('inf') or value == -float('inf'):
            return "Infinity"
        return f"{value:.6f}".rstrip('0').rstrip('.')
    except:
        return str(value)

# Generating a Markdown file for each ticker
for ticker in df.columns:
    # Sanitizing ticker name for filename
    safe_ticker = re.sub(r'[^\w\-]', '_', ticker)
    file_path = os.path.join(output_dir, f"{safe_ticker}.md")
    
    # Collecting metrics for the ticker
    metrics = []
    for metric, value in df[ticker].items():
        formatted_value = format_value(value)
        metrics.append(f"**{metric}**: {formatted_value}")
    
    # Creating Markdown content
    markdown_content = f"# {ticker}\n\n"
    markdown_content += "## Backtesting Metrics\n\n"
    markdown_content += "\n".join(metrics)
    
    # Writing to Markdown file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

print(f"Markdown files have been generated in the '{output_dir}' directory.")