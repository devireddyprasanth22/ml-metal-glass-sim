# ML to generate interatomic potentials
The MLP used to generate interatomic potentials was Allegro, an equivariant machine-learning interatomic potential (https://arxiv.org/abs/2204.05249) which is built as an extension to [NequIP](https://github.com/mir-group/nequip)

## Behind the scenes
At the base, Nequip is an equivariant graph neural network designed specifically for modeling atomistic systems. It leverages the principles of equivariance, meaning that its predictions remain consistent under transformations such as rotations, translations, and reflections. This property is crucial for accurately capturing the physical symmetries present in molecular and material systems. Nequip operates by representing atomic structures as graphs, where atoms serve as nodes and interatomic interactions are represented as edges. Using message-passing mechanisms and equivariant convolutions, Nequip efficiently learns complex potential energy surfaces and force fields, making it a powerful tool for simulating metallic glass formation.

![Equivariance](/images/equivariance.webp "Equivariance features")

## Requirements
* Python >= 3.9
* PyTorch >= 1.13. (Install pytorch before NequIP to prevent pip from trying to overwrite your PyTorch installation.)

## Input data
The input data used can be found in `train_data_siau.xyz`.

The format used is `extxyz` which contains not only the cartesian coordinates but also information of the lattice structure, forces and energy. `out2xyz.sh` was used to convert QE outputs to XYZ format

NequIP/Allegro takes in data that is ASE readable. More information can be found [here](https://wiki.fysik.dtu.dk/ase/ase/io/io.html)

## Process
For set up, please follow the steps outlined at the [Allegro repository](https://github.com/mir-group/allegro). If working on develop branch, ensure both Allegro and NequIP are clones from develop. This project used the develop branch. Reminder, Allegro and NequIP are under active development, so use the stable releases if unsure

To run:
`nequip-train -cn example.yaml`

The yaml file used can be found in this directory (siau.yaml)

Model was trained using resources at Setonix

Further information on set up and run can be found [here](https://nequip.readthedocs.io/en/develop/guide/install.html)

After training, use `nequip-deploy build` to build and deploy the `pth` file which creates an archive of its trained parameters and metadata (including interatomic potentials)
## References
* https://maurice-weiler.gitlab.io/blog_post/cnn-book_1_equivariant_networks/

* https://nequip.readthedocs.io/en/develop/guide/install.html
