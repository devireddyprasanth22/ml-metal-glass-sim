from ase.io import read, write

# Input and output file paths
input_file = "./combined.xyz"  # Replace with your actual file name and extension
output_file = ".filtered_combined.xyz"  # Replace with your desired output file name and extension
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    keep_block = False
    buffer = []
    last_number_line = None  # To store the line with the number before Lattice=

    for line in infile:
        if line.startswith("Lattice="):
            # Check if the previous block should be written
            if keep_block:
                if last_number_line:  # Write the number line if it exists
                    outfile.write(last_number_line)
                outfile.writelines(buffer)
            
            # Reset buffer and check for magmoms in the current line
            buffer = [line]
            keep_block = "magmoms" in line
        elif line.strip().isdigit():
            # Store the number line preceding Lattice=
            last_number_line = line
        else:
            # Add non-Lattice lines to the buffer
            buffer.append(line)
    
    # Write the last block if needed
    if keep_block:
        if last_number_line:  # Write the number line if it exists
            outfile.write(last_number_line)
        outfile.writelines(buffer)

print(f"Filtered configurations saved to {output_file}")