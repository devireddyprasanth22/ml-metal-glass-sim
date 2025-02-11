# Quantum Espresso
Quantum Espresso (QE) is an open-source suite of programs for quantum mechanical materials modeling based on density functional theory (DFT), plane waves, and pseudopotentials.

This folder contains the input files for QE dft calculations for amorphous SiAu. Crystalline structure can be found at [Materials Project](https://next-gen.materialsproject.org/materials/mp-1186998?chemsys=Au-Si) and is converted to QE input using [this](https://qeinputgenerator.materialscloud.io). Furthermore, scipts used to process various inputs to outputs can be found on quantum-espresso/data-proc 

Cif files can be visualised using VESTA, which was also used to create supercells and strained structures

## Process of Crystalline -> Amorphous

One of the processes that is applied to generate metallic glasses is a melt-quench technique, and this is the technique used in the project. This method involves heating a metallic alloy to a molten state and then rapidly cooling it at a rate high enough to prevent the formation of a crystalline structure. The rapid cooling locks the atoms in a disordered, amorphous state, forming a metallic glass.

![amorphization process](/images/Amorphization-process.png "amorphization process")

## Process on Quantum Espresso
On QE, for each configuration, we had three input files: relaxation, melt and quench. Some scripts in quantum-espresso/data-proc were used to automate the process. Resources at pawsey were used to run these simulations. Ensure that each run is able to access the pseduopotentials. The planewave function was used and the srun command on the cluster allowed for MPI parallelizationx
`srun -n 32 pw.x < input file &> output file &`

More information on input file description can be found [here](https://www.quantum-espresso.org/Doc/INPUT_PW.html)