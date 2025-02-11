from ase.io import read, write

example_atoms = read('../data/xyz_inputs/train_data_siau.xyz', index=0)
write('./siau_quenched.data', example_atoms, format='lammps-data')