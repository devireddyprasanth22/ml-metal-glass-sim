#!/bin/bash

INPUT_DIR="/path/to/your/cif/files"
OUTPUT_DIR="/path/to/output/directory"
PYTHON_SCRIPT="/path/to/your/python_script.py"
VAC_LOOP=5

mkdir -p "$OUTPUT_DIR"

for cif_file in "$INPUT_DIR"/*.cif; do
    if [[ -f "$cif_file" ]]; then
        echo "Processing $cif_file..."
        python "$PYTHON_SCRIPT" "$cif_file" "$VAC_LOOP" "$OUTPUT_DIR"
    fi
done

echo "All files processed. Outputs are in $OUTPUT_DIR."

