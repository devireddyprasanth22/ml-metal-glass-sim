# LAMMPS for MD simulation
LAMMPS, a highly scalable molecular dynamics (MD) simulator, was used to simulate the formation of amourphous gold-silicon after training Allegro. Allegro.

`pair_allegro` is the LAMMPS pair style support for Allegro. pair_allegro also support MPI 

This directory has `rdfPlot.ipynb` to plot rdf, `si3au10.rdf` which is the rdf of a particular amorphous gold silicon structure, `siau_deployed.pth` which is the doployed model, and `xyz2data.py` to convert files

## Usage
Update LAMMPS input with:
```
pair_style	allegro 
pair_coeff	* * deployed.pth <Allegro type name for LAMMPS type 1> <Allegro type name for LAMMPS type 2> ...
```

## Building LAMMPS
- Download LAMMPS

    `git clone --depth=1 https://github.com/lammps/lammps`
- Download pair-allegro

    `git clone https://github.com/mir-group/pair_allegro`
- Patch LAMMPS with pair_allegro

    `./patch_lammps.sh /path/to/lammps/`
- If using Pytorch (with NVIDIA or CPU)

    ```
    cd lammps
    mkdir build
    cd build
    cmake ../cmake -DCMAKE_PREFIX_PATH=`python -c 'import torch;print(torch.utils.cmake_prefix_path)'`
    ```
- If using Pytorch (with AMD/HIP)

    ```
    mkdir build
    cd build
    export LC_ALL=C.UTF-8
    cmake ../cmake -DCMAKE_PREFIX_PATH=`python3 -c 'import torch;print(torch.utils.cmake_prefix_path)'`
    ```

For further information, please follow steps outlined on the [pair_allegro repo](https://github.com/mir-group/pair_allegro)

## Notes
- To avoid issues such as 
    ``` 
    instance of 'c10::Error'
     what():  isTuple()INTERNAL ASSERT FAILED
     ```
    ensure that Allegro and LAMMPS are built in the same version of torch (>1.13)


- If you encounter error like 
    ```
    Exception: expected scalar type Double but found Float
    ```
    change to `pair_style allegro3232` or `pair_style allegro6464`, depending what the model dtype is. Or retrain with `default_dtype: float64` in config.yaml for Allegro

## References
* https://lammpstutorials.github.io
* https://github.com/lammps/lammps
* https://docs.lammps.org/Manual.html