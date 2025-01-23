#!/bin/bash

input_dir=$1

for file in "$input_dir"/*.out; do
    base_name=$(basename "$file" .out)
    out_file="${input_dir}/${base_name}.xyz"
    echo "Processing $file -> $out_file"
    ase convert -n -1 "$file" "$out_file"
done
echo "all done"
