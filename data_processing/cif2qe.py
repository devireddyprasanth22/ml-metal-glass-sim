import sys
import os
from ase.io import read
import math

""" Script for converting cif data to qe data from a template file of the given configuration"""

def compute_cell_params(cell):
    """convert from primitive cell to lattice coords"""
    a = cell[0]
    b = cell[1]
    c = cell[2]
    alpha_rad = math.radians(cell[3])
    beta_rad = math.radians(cell[4])
    gamma_rad = math.radians(cell[5])

    ax, ay, az = a, 0, 0
    bx, by, bz = b * math.cos(gamma_rad), b * math.sin(gamma_rad), 0
    cx = c * math.cos(beta_rad)
    cy = c * (math.cos(alpha_rad) - math.cos(beta_rad) * math.cos(gamma_rad)) / math.sin(gamma_rad)
    cz = c * math.sqrt(1 - math.cos(beta_rad)**2 - ((math.cos(alpha_rad) - math.cos(beta_rad) * math.cos(gamma_rad)) / math.sin(gamma_rad))**2)

    return [(ax, ay, az), (bx, by, bz), (cx, cy, cz)]

def extract_cif_data(cif_file):
    """extract data from cif file"""
    structure = read(cif_file)
    cell = structure.cell.cellpar()
    atomic_positions = structure.get_scaled_positions()
    symbols = structure.get_chemical_symbols()
    nat = len(symbols)

    return cell, atomic_positions, symbols, nat

def cif2qe(cif_file):
    cell, atomic_positions, symbols, nat = extract_cif_data(cif_file)
    template = """
&CONTROL
  calculation = 'vc-relax'
  etot_conv_thr =   1.6000000000d-04
  forc_conv_thr =   1.0000000000d-04
  outdir = './out/'
  prefix = 'aiida'
  pseudo_dir = './pseudo/'
  tprnfor = .true.
  tstress = .true.
/
&SYSTEM
  degauss =   2.7500000000d-02
  ecutrho =   2.4000000000d+02
  ecutwfc =   4.5000000000d+01
  ibrav = 0
  nat = {nat}
  nosym = .false.
  ntyp = 2
  occupations = 'smearing'
  smearing = 'cold'
/
&ELECTRONS
  conv_thr =   3.2000000000d-09
  electron_maxstep = 80
  mixing_beta =   4.0000000000d-01
/
&IONS
  ion_dynamics = 'bfgs'
/
&CELL
  cell_dynamics = 'bfgs'
/
ATOMIC_SPECIES
Au     196.966569 Au_ONCV_PBEsol-1.0.upf
Si     28.0855 Si.pbesol-n-rrkjus_psl.1.0.0.UPF
ATOMIC_POSITIONS crystal
{atomic_positions}
K_POINTS automatic
2 2 2 0 0 0
CELL_PARAMETERS angstrom
{cell_parameters}
"""

    # Format atomic positions
    atomic_positions_str = "\n".join(
        f"{symbols[i]}     {pos[0]:.10f}     {pos[1]:.10f}     {pos[2]:.10f}"
        for i, pos in enumerate(atomic_positions)
    )

    # Compute cell parameters
    new_cell = compute_cell_params(cell)
    cell_parameters_str = "\n".join(
        f"      {v[0]:.10f}       {v[1]:.10f}       {v[2]:.10f}" for v in new_cell
    )

    # Format the template
    formatted_template = template.format(
        nat=nat,
        atomic_positions=atomic_positions_str,
        cell_parameters=cell_parameters_str,
    )

    output_file = os.path.splitext(os.path.basename(cif_file))[0]
    output_file = f'{output_dir}/{output_file}.in'
    # Write to output file
    with open(output_file, 'w') as file:
        file.write(formatted_template)

if __name__ == "__main__":
    # a for loop that will convert all cif files to output files in a dir

    cif_file = sys.argv[1]
    output_dir = sys.argv[2]

    os.makedirs(output_dir, exist_ok=True)
    cif2qe(cif_file,output_dir)


