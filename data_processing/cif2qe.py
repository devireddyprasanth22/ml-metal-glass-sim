import os
import re
from ase.io import read
""" Script for converting cif data to qe data from a template file of the given configuration"""
def extract_cif_data(cif_file):
    """Extracts atomic positions, cell parameters, and number of atoms from a CIF file."""
    structure = read(cif_file)
    cell = structure.cell
    atomic_positions = structure.get_scaled_positions()
    symbols = structure.get_chemical_symbols()
    nat = len(symbols)

    return cell, atomic_positions, symbols, nat

def cif2qe(template_file, output_file, cell, atomic_positions, symbols, nat):
    with open(template_file, 'r') as file:
        template = file.read()

    # Update nat
    template = re.sub(r'(\bnat\s*=\s*)\d+', f'\\g<1>{nat}', template)

     # Update ATOMIC_POSITIONS
    atomic_positions_str = "\n".join(
        f"{symbols[i]}     {pos[0]:.10f}     {pos[1]:.10f}     {pos[2]:.10f}"
        for i, pos in enumerate(atomic_positions)
    )
    template = re.sub(r'(ATOMIC_POSITIONS\s+crystal\n)([\s\S]+?)(\n\n|$)', f'\\1{atomic_positions_str}\\3', template)
    
    # update k-points (manually if not in template)
    if "K_POINTS" not in template:
        template += "\nK_POINTS automatic\n2 2 2 0 0 0\n"
    
    # Update CELL_PARAMETERS
    cell_str = "\n".join(
        f"      {cell[i][0]:.10f}       {cell[i][1]:.10f}       {cell[i][2]:.10f}" 
        for i in range(3)
    )
    if "CELL_PARAMETERS" in template:
        template = re.sub(r'(CELL_PARAMETERS\\s+angstrom\\n)([\\s\\S]+?)(\\n\\n|$)', f'\\1{cell_str}\\3', template)
    else:
        template += f"\nCELL_PARAMETERS angstrom\n{cell_str}\n"
    
    # Write the updated template to the output file
    with open(output_file, 'w') as file:
        file.write(template)

if __name__ == "__main__":

    cif_file = "/Users/dp/Desktop/pawsey/pawsey-internship/Crystalline_conf_SiAu/SiAu3_cubic/SiAu3_odd_au_vac.cif"  # Path to your CIF file
    template_file = "/Users/dp/Desktop/pawsey/pawsey-internship/Crystalline_conf_SiAu/SiAu3_cubic/qe_input/SiAu3.in"  # Path to your QE input template
    output_file = "/Users/dp/Desktop/pawsey/pawsey-internship/Crystalline_conf_SiAu/SiAu3_cubic/test.in"  # Path to the output QE input file

    cell, atomic_positions, symbols, nat = extract_cif_data(cif_file)

    cif2qe(template_file, output_file, cell, atomic_positions, symbols, nat)

    print(f"QE input file updated: {output_file}")
