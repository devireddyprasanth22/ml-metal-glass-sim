#!/bin/bash

INPUT_DIR="/Users/dp/Desktop/pawsey/pawsey-internship/vacancies_siau3"
OUTPUT_DIR="/Users/dp/Desktop/pawsey/pawsey-internship/relaxation"
PYTHON_SCRIPT="./cif2qe.py"

mkdir -p "$OUTPUT_DIR"

for cif_file in "$INPUT_DIR"/*.cif; do
    if [[ -f "$cif_file" ]]; then
        echo "converting to qe input relaxation $cif_file"
        python "$PYTHON_SCRIPT" "$cif_file" "$OUTPUT_DIR"
    fi
done
echo "converted all file form $INPUT_DIR to relaxed inputs in $OUTPUT_DIR"
