#!/bin/bash

INPUT_DIR="/"
OUTPUT_DIR="/"
PYTHON_SCRIPT="./generate_vac.py"
VAC_LOOP=31

mkdir -p "$OUTPUT_DIR"

for cif_file in "$INPUT_DIR"/*.cif; do
    if [[ -f "$cif_file" ]]; then
        echo "Processing $cif_file..."
        python "$PYTHON_SCRIPT" "$cif_file" "$VAC_LOOP" "$OUTPUT_DIR"
    fi
done

echo "All files processed. Outputs are in $OUTPUT_DIR."

