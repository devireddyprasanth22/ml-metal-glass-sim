#!/bin/bash

OUT_DIR="/" #the output files from the previous run, corresponfing input files in INP_DIR
INP_DIR="/" #the input files that result in out in OUT_DIR
NEW_INP_DIR="/" #new inputs will be written to this folder
TYPE="quench" #melt or quench
PYTHON_SCRIPT="./out2in.py"

mkdir -p "$NEW_INP_DIR"

for inp_file in "$INP_DIR"/*.in; do
    base_name=$(basename "$inp_file" .in)
    out_file="$OUT_DIR/${base_name}.out"
    if [[ -f "$out_file" ]]; then
        python "$PYTHON_SCRIPT" "$inp_file" "$NEW_INP_DIR" "$TYPE" "$out_file"
    else
        echo "Warning: Output file $out_file not found for input $inp_file. Skipping."
    fi
done

echo "Processing complete. New input files are in $NEW_INP_DIR."
