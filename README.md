# AlphaFold 3 Tutorial Series

This repository contains a step-by-step guide to running and interpreting predictions using **AlphaFold 3**, with a focus on real protein–ligand systems. These tutorials are designed for researchers, developers, and students interested in structure prediction, drug discovery, and computational biology.

------

## Walkthrough Overview

This tutorial series starts with a **walkthrough**, which provides a high-level introduction to the model’s architecture, key modules (Pairformer and diffusion), and important features such as recycling, confidence metrics, and handling of small molecules. This walkthrough is designed to be installation-free and server-based, making it easy for users to get started without any local installations.

> [Open the Walkthrough in Colab](https://colab.research.google.com/github/richcmwang/AlphaFold-3-Tutorial-Series/blob/main/tutorials/af3_walkthrough.ipynb)

------

## Available Tutorial

### [1. Predicting ATP-Bound PKA (1ATP)](https://colab.research.google.com/github/richcmwang/AlphaFold-3-Tutorial-Series/blob/main/tutorials/af3_1ATP_server_tutorial.ipynb)

Learn how to:

- Use the AlphaFold 3 server to predict a protein–ligand complex
- Visualize the results with **ChimeraX** (offline screenshots provided)
- Compare the predicted structure with the crystal structure (PDB: 1ATP)
- Zoom into the ligand binding site and compute RMSD
- Interpret structural confidence using pLDDT and PAE

> This tutorial includes some Python code to display results and guide analysis, but no local AlphaFold 3 or Docker installation is required. ChimeraX is optional but recommended for offline exploration.

------

## Coming Soon

### [2. Running AlphaFold 3 Locally: 7M41 with Custom Ligand YQG]

This upcoming tutorial will show how to:

- Install and run AlphaFold 3 locally
- Model systems **not supported by the AF3 server**, such as ligands outside the CCD whitelist
- Reproduce the protein–ligand structure of **7M41** including custom ligand **YQG**

------

## What You’ll Learn

- How to run AlphaFold 3 for protein–ligand systems
- How to visualize and align predicted structures using ChimeraX
- How to assess prediction quality using pLDDT, PAE, and RMSD
- Best practices for structure validation and interpretation

------

## Requirements

- ChimeraX (for offline visualization)
- AlphaFold 3 server access (for walkthrough and 1ATP tutorial)
- Python + Docker (for local runs — covered in tutorial 2)

------

## Getting Started

Clone the repository and begin with the walkthrough or the 1ATP tutorial:

```bash
git clone https://github.com/richcmwang/AlphaFold-3-Tutorial-Series.git
cd tutorials
```

Open the walkthrough here:
 `tutorials/af3_walkthrough.ipynb`

Or open the first tutorial here:
 `tutorials/af3_1ATP_server_tutorial.ipynb`
