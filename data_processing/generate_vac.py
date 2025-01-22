import os

import random
"""
Script for generating random vacancies in a cif file for creating more data
"""
def create_vacancy(input_file, output_file, num_vac):
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
    remove_idx = random.sample(range(len(atom_lines)), num_vac)
    new_atom_lines = [at for idx,at in enumerate(atom_lines) if idx not in remove_idx]
    new_lines = lines[:atom_start] + new_atom_lines

    with open(output_file, 'w') as f:
        f.writelines(new_lines)
    
    print(f"vacancies saved to {output_file}")

def process_vacancies(input_file, vac_loop):
    filename = os.path.splitext(os.path.basename(input_file))[0]
    for i in range(vac_loop):
        output_file = f'{filename}_vac{i}.in'
        with open(f'{output_file}', 'w') as f:
            pass
        create_vacancy(input_file, output_file, i)


file_in = "/Users/dp/Desktop/pawsey/pawsey-internship/Crystalline_conf_SiAu/SiAu3_cubic/SiAu3_211.cif"
vac_loop = 10 # 1 vac up until 10 vacs
process_vacancies(file_in, vac_loop)