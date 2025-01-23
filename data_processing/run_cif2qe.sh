#!/bin/bash

INPUT_DIR=""
OUTPUT_DIR=""
PYTHON_SCRIPT="/path/to/your/python_script.py"
mkdir -p "$OUTPUT_DIR"
for cif_file in "$INPUT_DIR/*.cif"; do
    if [[-f "$cif_file"]]; then
        echo "converting to qe input relaxation $cif_file"
        python "$PYTHON_SCRIPT" "$cif_file" "$OUTPUT_DIR"
    fi
done
echo "converted all file form $INPUT_DIR to relaxed inputs in $OUTPUT_DIR"