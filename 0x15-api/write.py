import csv

# Sample data (list of dictionaries)
data = [
    {"Name": "John", "Age": 30, "City": "New York"},
    {"Name": "Alice", "Age": 25, "City": "Chicago"},
    {"Name": "Bob", "Age": 35, "City": "Los Angeles"}
]

# Specify the CSV file name
csv_file = "output.csv"

# Export data to CSV
try:
    with open(csv_file, "w", newline="") as csvfile:
        # Define CSV header
        fieldnames = ["Name", "Age", "City"]
        
        # Create a CSV DictWriter object
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header to the CSV file
        csv_writer.writeheader()
        
        # Write data rows to the CSV file
        csv_writer.writerows(data)
        
    print(f"Data exported to {csv_file} successfully.")
except Exception as e:
    print(f"Error: {str(e)}")

