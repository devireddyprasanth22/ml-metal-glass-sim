#!/bin/bash

INPUT_DIR="/"
out_dir="/"

for file in "$INPUT_DIR"/*.out; do
    base_name=$(basename "$file" .out)
    out_file="${out_dir}/${base_name}.xyz"
    echo "Processing $file -> $out_file"
    ase convert -n 95:100 "$file" "$out_file"
done
echo "all done"
