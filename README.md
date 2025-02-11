# Machine learning for simulating formation of metallic glasses
This repository documents the process, data, and scripts used to apply machine learning techniques for simulating the formation of metallic glasses, specifically Gold-Silicon, as part of my Pawsey internship. 

## Introduction

Metallic glasses are amorphous metal alloys with unique mechanical and thermal properties. Traditional techniques of simulation (Density Functional Theorem) are computationally expensive, whilst machine learning offers a faster and scalable technqiue to modelling metallic glasses.
This project explores the use of machine learning to simulate and predict their formation, leveraging computational techniques and high-performance computing.

## Repo structure
This repository is broken into 3 sections: 
- quantum-espresso which contains data and process employed for generating amorphous structures for training ML model
- ml-model which includes details of the ml model employed and the steps required for set-up
- lammps-md which includes details of set up and process employed to simulating structures using interatomic potentials
