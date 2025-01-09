# Quantum Espresso MD input files



This folder contains the input files for QE md for amorphous SiAu3. Crystalline structure can be found at [Materials Project](https://next-gen.materialsproject.org/materials/mp-1186998?chemsys=Au-Si) and is converted to QE input using [this](https://qeinputgenerator.materialscloud.io). Then this structure is used to perform relaxation before melting and quenching using the respective files. The structure from the output needs to be the input for the next run (relaxation -> melt -> quench)

To run on setonix, here are the steps:
1. `salloc -p work -n 32 -N 1 -c 2 --mem=115G -A Interns202411`
2. `module load quantum-espresso/7.2`
3. `srun -n 32 pw.x < input file &> output file &`
4. `tail -f output file`