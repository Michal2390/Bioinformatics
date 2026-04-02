# De Novo DNA Assembly

This repository contains coursework materials for the MBI laboratory on de novo DNA assembly.

## What This Project Is
This project documents a practical bioinformatics workflow for short-read assembly:
1. simulate paired-end sequencing reads,
2. run de novo assembly,
3. evaluate assembly quality,
4. calculate GC-content with a custom script.

## Why This Project Exists
The goal is to practice the full assembly pipeline end-to-end and learn how to interpret key quality metrics (for example N50, genome fraction, mismatches/indels, and misassemblies).

## Repository Contents
- `lab1/` - complete Lab 1 materials:
  - GC-content script (`lab1/scripts/gc_content.py`)
  - script test (`lab1/tests/test_gc_content.py`)
  - working report (`lab1/sprawozdanie_lab1_draft.md`)
  - QUAST outputs (`lab1/output/quast_results/`)
- `lab2/` - complete Lab 2 materials (DNA annotation):
  - scaffold selection, masking, and GFF stats scripts
  - amino acid to RNA conversion task with tests
  - completed lab report (`lab2/sprawozdanie_lab2_draft.md`)
  - selected lightweight outputs (GFF, BLAST query/results, summaries)

## Quick Start
Detailed run instructions and parameters are available in:
- `lab1/README.md`
- `lab2/README.md`

## Notes
The repository stores lightweight artifacts (source code and text reports).
Large generated data files are intentionally excluded via `.gitignore`.
