## Data processing for QE
1) Generate CIF file
2) run generate vacancies bash file (after adjusting inputs)
3) step 2 creates n files with n vacancies in X dir
4) now run cif2qe bash file (adjust inputs)
5) step 4 takes in X dir and converts all files to relaxation inputs in Y dir
6) Run relaxation and store outputs in Z dir
7) now run qe out2in bash script (adjust inputs)
8) step 7 creates either melt inputs or quench inputs based on whats been passed as inputs and these new inputs will be stored in a new dir A
9) run melt or quench
10) If melt, repeat step 7 by adjusting inputs; elif quench, get quench out files