import os
import csv

#Hardcoded paths
photos_folder = "path/to/folder"
csv_file_path = "path/to/csv"

# Read the CSV and perform the renaming
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) < 2:
            print(f"Skipping incomplete row: {row}")
            continue

        old_name = row[0].strip()
        new_name = row[1].strip()

        if not new_name.lower().endswith(".jpg"):
            new_name += ".jpg"

        old_path = os.path.join(photos_folder, old_name)
        new_path = os.path.join(photos_folder, new_name)

        try:
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                print(f"Renamed: {old_name} -> {new_name}")
            else:
                print(f"File not found: {old_name}")
        except Exception as e:
            print(f"Error renaming {old_name} to {new_name}: {e}")
