#!/bin/bash

INPUT_DIR="/Users/dp/Desktop/pawsey/pawsey-internship/test_siau3"
OUTPUT_DIR="/Users/dp/Desktop/pawsey/pawsey-internship/vacancies_siau3/"
PYTHON_SCRIPT="./generate_vac.py"
VAC_LOOP=5

mkdir -p "$OUTPUT_DIR"

for cif_file in "$INPUT_DIR"/*.cif; do
    if [[ -f "$cif_file" ]]; then
        echo "Processing $cif_file..."
        python "$PYTHON_SCRIPT" "$cif_file" "$VAC_LOOP" "$OUTPUT_DIR"
    fi
done

echo "All files processed. Outputs are in $OUTPUT_DIR."

