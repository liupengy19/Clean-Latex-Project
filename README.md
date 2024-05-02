# Clean-Latex-Project
This simple Python script removes unused files in a Latex project.

This script iterates over all files in the project folder. If a file is not contained in the compilation log, it is viewed as not used.

## Usage
Compile the project to generate a log.

Run 
```bash
python clean_latex_project.py {project_folder} {main_filename (do not include .log)}
```
