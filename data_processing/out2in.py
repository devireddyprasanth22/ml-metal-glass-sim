import re

def extract_final_atomic_positions(file_path):
    """
    Extracts the atomic positions from the last iteration of a QE output file.

    Parameters:
        file_path (str): Path to the QE output file.

    Returns:
        str: The atomic positions block from the last iteration.
    """
    with open(file_path, "r") as f:
        content = f.read()

    # Regex to match all ATOMIC_POSITIONS blocks
    pattern = r"ATOMIC_POSITIONS\s+\(.*?\)\n([\s\S]+?)(?=\n\n|$)"
    matches = re.findall(pattern, content)

    if matches:
        # Return the last match (final iteration)
        return matches[-1].strip()
    else:
        raise ValueError("No ATOMIC_POSITIONS block found in the file.")

# Example usage
qe_output_file = "/Users/dp/Desktop/pawsey/PWscf_cubic/SiAu_melt.out"  # Replace with the path to your QE output file

try:
    final_positions = extract_final_atomic_positions(qe_output_file)
    print("Final Atomic Positions:")
    print(final_positions)
except ValueError as e:
    print(e)
