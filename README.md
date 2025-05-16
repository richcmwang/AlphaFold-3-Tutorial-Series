# AlphaFold 3 Tutorial Series

This repository contains a step-by-step guide to running and interpreting predictions using **AlphaFold 3**, with a focus on real protein–ligand systems. These tutorials are designed for researchers, developers, and students interested in structure prediction, drug discovery, and computational biology.

---

## Available Tutorial

### [1. Predicting ATP-Bound PKA (1ATP)](tutorials/af3_1ATP_server_tutorial.ipynb)
Learn how to:
- Use the AlphaFold 3 server to predict a protein–ligand complex
- Visualize the results with **ChimeraX**
- Compare the predicted structure with the crystal structure (PDB: 1ATP)
- Zoom into the ligand binding site and compute RMSD
- Interpret structural confidence using pLDDT and PAE

> This tutorial also includes a practical introduction to ChimeraX for alignment and ligand analysis.

---

## Coming Soon

### [2. Running AlphaFold 3 Locally: 7M41 with Custom Ligand YQG]
This upcoming tutorial will show how to:
- Install and run AlphaFold 3 locally
- Model systems **not supported by the AF3 server**, such as ligands outside the CCD whitelist
- Reproduce the protein–ligand structure of **7M41** including custom ligand **YQG**

---

## What You’ll Learn

- How to run AlphaFold 3 for protein–ligand systems
- How to visualize and align predicted structures using ChimeraX
- How to assess prediction quality using pLDDT, PAE, and RMSD
- Best practices for structure validation and interpretation

---

## Requirements

- ChimeraX (for visualization)
- AlphaFold 3 access (server or local)
- Python + Docker (for local runs — covered in tutorial 2)

---

## Getting Started

Clone the repository and begin with the 1ATP tutorial:

```bash
git clone https://github.com/richcmwang/AlphaFold-3-Tutorial-Series.git
cd tutorials
```

Open the first tutorial here:  
`tutorials/af3_1ATP_server_tutorial.ipynb`
