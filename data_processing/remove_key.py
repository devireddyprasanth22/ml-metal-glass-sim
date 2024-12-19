from ase.io import read, write

# Input and output file paths
input_file = "./combined.xyz"  # Replace with your actual file name and extension
output_file = ".filtered_combined.xyz"  # Replace with your desired output file name and extension

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    keep_block = False
    buffer = []
    
    for line in infile:
        if line.startswith("Lattice="):
            # Check if the previous block should be written
            if keep_block:
                outfile.writelines(buffer)
            
            # Reset buffer and check for magmoms in the current line
            buffer = [line]
            keep_block = "magmoms" in line
        else:
            # Add non-Lattice lines to the buffer
            buffer.append(line)
    
    # Write the last block if needed
    if keep_block:
        outfile.writelines(buffer)

print(f"Filtered configurations saved to {output_file}")