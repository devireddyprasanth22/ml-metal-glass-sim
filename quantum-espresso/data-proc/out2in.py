import re
import sys
import os
"""
Script to convert from qe output to melt input or quench input
"""
def extract_final_atomic_positions(output_file_path):
    """
    Extracts the atomic positions from the last iteration of a QE output file.
    """
    with open(output_file_path, "r") as f:
        content = f.read()

    # Regex to match all ATOMIC_POSITIONS blocks
    pattern_pos = r"ATOMIC_POSITIONS\s+\(.*?\)\n([\s\S]+?)(?=\n\n|$)"
    matches_pos = re.findall(pattern_pos, content)

    #Regex to match all CELL_PARAMETERS blocks
    pattern_cell = r"CELL_PARAMETERS\s+\(.*?\)\n([\s\S]+?)(?=\n\n|$)"
    matches_cell = re.findall(pattern_cell, content)

    if matches_cell and matches_pos:
        return matches_pos[-1].strip(), matches_cell[-1].strip()
    elif matches_pos:
        return matches_pos[-1].strip()

    else:
        raise ValueError("No ATOMIC_POSITIONS block found in the file.")

def update_input(input_file, new_input_dir, type, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    positions, *pos_cell = extract_final_atomic_positions(output_file)
    cell = pos_cell[0] if pos_cell else None
    content = re.sub(
    r"(ATOMIC_POSITIONS\s+[\w()]*\n)([\s\S]*?)(?=K_POINTS|$)",
    f"\\1{positions}\n",
    content,
)

# Update positions in input file
# if vc-md (melt), change calculation and add dt = 20 and nstep = 100, change &IONS to temperature = 'initial', ion_dynamics = beeman, tempw = 2000 and add &CELL and change cell_dynamics - 'pr'
# if md (quench), change ion_temp = 'reduce-T', delta_t = -34, nraise = 2, and remove &CELL
    if type == "melt":
        # Update calculation type
        content = re.sub(r"calculation\s*=\s*['\"].*?['\"]", "calculation = 'vc-md'", content)

        if "dt" in content:
            content = re.sub(r"dt\s*=\s*\d+", "dt = 20", content)
        else:
            content = re.sub(r"(\&CONTROL[\s\S]*?)(\n/)", r"\1\n  dt = 20\2", content)

        if "nstep" in content:
            content = re.sub(r"nstep\s*=\s*\d+", "nstep = 100", content)
        else:
            content = re.sub(r"(\&CONTROL[\s\S]*?)(\n/)", r"\1\n  nstep = 100\2", content)

        if "ion_dynamics" in content:
            content = re.sub(r"ion_dynamics\s*=\s*['\"].*?['\"]", "ion_dynamics = 'beeman'", content)
        else:
            content = re.sub(r"(\&IONS[\s\S]*?)(\n/)", r"\1\n  ion_dynamics = 'beeman'\2", content)

        if "tempw" in content:
            content = re.sub(r"tempw\s*=\s*\d+", "tempw = 2000", content)
        else:
            content = re.sub(r"(\&IONS[\s\S]*?)(\n/)", r"\1\n  tempw = 2000\2", content)

        if "ion_temperature" in content:
            content = re.sub(r"ion_temperature\s*=\s*['\"].*?['\"]", "ion_temperature = 'initial'", content)
        else:
            content = re.sub(r"(\&IONS[\s\S]*?)(\n/)", r"\1\n  ion_temperature = 'initial'\2", content)

        if "&CELL" not in content:
            content += "\n&CELL\n  cell_dynamics = 'pr'\n/\n"
        else:
            content = re.sub(r"(cell_dynamics\s*=\s*['\"].*?['\"])", "cell_dynamics = 'pr'", content)

    elif type == "quench":
        # Update calculation type
        content = re.sub(r"calculation\s*=\s*['\"].*?['\"]", "calculation = 'md'", content)

        if "ion_dynamics" in content:
            content = re.sub(r"ion_dynamics\s*=\s*['\"].*?['\"]", "ion_dynamics = 'verlet'", content)
        else:
            content = re.sub(r"(\&IONS[\s\S]*?)(\n/)", r"\1\n  ion_dynamics = 'verlet'\2", content)
        # Add or update parameters in &IONS
        if "ion_temperature" in content:
            content = re.sub(r"ion_temperature\s*=\s*['\"].*?['\"]", "ion_temperature = 'reduce-T'", content)
        else:
            content = re.sub(r"(\&IONS[\s\S]*?)(\n/)", r"\1\n  ion_temperature = 'reduce-T'\2", content)

        if "delta_t" in content:
            content = re.sub(r"delta_t\s*=\s*-?\d+", "delta_t = -34", content)
        else:
            content = re.sub(r"(\&IONS[\s\S]*?)(\n/)", r"\1\n  delta_t = -34\2", content)

        if "nraise" in content:
            content = re.sub(r"nraise\s*=\s*\d+", "nraise = 2", content)
        else:
            content = re.sub(r"(\&IONS[\s\S]*?)(\n/)", r"\1\n  nraise = 2\2", content)

        # Remove &CELL section if present
        content = re.sub(r"&CELL[\s\S]*?/\n", "", content)

        #update cell_parameters if quench from melt
        content = re.sub(r"CELL_PARAMETERS\s+angstrom\s*\n([\s\S]+?)(?=\n\n|$)", f"CELL_PARAMETERS angstrom \n\1   {cell}\n", content)

    else:
        raise ValueError("Invalid type. Supported types are 'vc-md' (melt) and 'md' (quench).")

    filename = os.path.splitext(os.path.basename(input_file))[0]
    new_input_file = f'{new_input_dir}/{filename}_{type}.in'
    # Write to the new input file
    with open(new_input_file, 'w') as file:
        file.write(content)


if __name__ == "__main__": 

    input_file =  sys.argv[1]
    new_input_dir = sys.argv[2]
    type_of_calculation = sys.argv[3]
    output_file = sys.argv[4]
    
    update_input(input_file,new_input_dir,type_of_calculation,output_file)