import os
import sys
import random
"""
Script for generating random vacancies in a cif file for creating more data
"""
def create_vacancy(input_file, output_file, num_vac, n=5):
    with open(input_file, 'r') as f:
        lines = f.readlines()


    atom_start = None
    atom_end = None
    atom_lines = []

    for idx, line in enumerate(lines):
        if "_atom_site_type_symbol" in line:
            atom_start = idx + 1
            break
    
    if atom_start is None:
        print(f"line not found in {input_file}")
    
    atom_lines = lines[atom_start:]

    all_vacancy_sets = []
    for _ in range(n):
        remove_idx = random.sample(range(len(atom_lines)), num_vac)
        new_atom_lines = [at for idx,at in enumerate(atom_lines) if idx not in remove_idx]
        all_vacancy_sets.append(new_atom_lines)

    for i, new_atom_lines in enumerate(all_vacancy_sets):
        new_lines = lines[:atom_start] + new_atom_lines
        output_file_set = output_file.replace('.cif', f'_set{i+1}.cif')
        with open(output_file_set, 'w') as f:
            f.writelines(new_lines)
        print(f"Vacancy set {i+1} saved to {output_file_set}")

def process_vacancies(input_file, vac_loop, out_dir):
    filename = os.path.splitext(os.path.basename(input_file))[0]
    for i in range(vac_loop):
        output_file = f'{out_dir}/{filename}_vac{i}.cif'
        with open(f'{output_file}', 'w') as f:
            pass
        create_vacancy(input_file, output_file, i)


if __name__ == "__main__":
    input_file = sys.argv[1]
    vac_loop = int(sys.argv[2])
    out_dir = sys.argv[3]

    process_vacancies(input_file, vac_loop, out_dir)