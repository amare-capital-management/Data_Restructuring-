<img width="780" height="253" alt="ACM w color" src="https://github.com/user-attachments/assets/a986f602-8703-464f-9426-cc3e9f5ffbc8" />

### This script, 7.Data_Restructuring. is designed to read backtesting results from a CSV file and generate Markdown files for each stock ticker, summarizing the metrics in a clean and readable format. Here's a breakdown of what the code does:

*1. Setup and Directory Creation:*

Creates an output directory named backtesting to store the generated Markdown files.
If the directory doesn’t already exist, it is created using os.makedirs().

*2. Reading the CSV File:*
   
Reads a CSV file named output.csv into a Pandas DataFrame (df), where:
Columns represent stock tickers.
Rows represent various metrics for each ticker.

*3. Value Formatting:*
   
Defines a function format_value(value) to clean and format the values:
Converts numerical values to six decimal places, removing trailing zeros.
Handles NaN values by replacing them with "N/A".
Converts infinite values to "Infinity".
Leaves non-numeric values as strings.

*4. Markdown File Generation:*

Iterates over each column (ticker) in the DataFrame:
Sanitizes the ticker name to ensure it is safe for use as a filename (e.g., replaces special characters with underscores).
Collects all metrics and their formatted values for the ticker.
Creates a Markdown file for each ticker with the following structure:
Title: The ticker name.
Section: "Backtesting Metrics" with a list of metrics and their values.
Writes the Markdown content to a file in the backtesting directory.

*5. Output:*
Prints a confirmation message once all Markdown files have been generated.

*Purpose:*

This script is a data restructuring tool designed to:
Convert backtesting results stored in a CSV file into individual Markdown files for each stock ticker.
Provide a clean and organized summary of metrics for each ticker in a human-readable format.
