import os
import re

SECTION_ORDER = [
    "&CONTROL",
    "&SYSTEM",
    "&ELECTRONS",
    "&IONS",
    "&CELL",
    "ATOMIC_SPECIES",
    "ATOMIC_POSITIONS",
    "K_POINTS",
    "CELL_PARAMETERS"
]

def organize_qe_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Dictionary to hold sections
    sections = {key: [] for key in SECTION_ORDER}
    other_lines = []
    current_section = None

    # Parse file into sections
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith(tuple(SECTION_ORDER)):
            current_section = next((sec for sec in SECTION_ORDER if stripped_line.startswith(sec)), None)
            sections[current_section].append(line)
        elif stripped_line.startswith('/') and current_section:
            sections[current_section].append(line)
            current_section = None
        elif current_section:
            sections[current_section].append(line)
        else:
            other_lines.append(line)

    # Combine sections in the correct order
    organized_content = []
    for section in SECTION_ORDER:
        if sections[section]:
            organized_content.extend(sections[section])
    organized_content.extend(other_lines)  # Append uncategorized lines (if any)

    with open(file_path, 'w') as f:
        f.writelines(organized_content)

def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                organize_qe_file(file_path)
                print(f"Processed: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Specify the directory containing Quantum ESPRESSO input files
directory_path = "/Users/dp/Desktop/pawsey/pawsey-internship/super_melt/"  # Replace with your directory path
process_directory(directory_path)
