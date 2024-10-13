import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

# Create the repo and files
for filepath in list_of_files:
    # Créer le chemin complet du fichier
    filepath = Path(filepath)

    # Créer le répertoire parent s'il n'existe pas
    filedir = filepath.parent
    if not filedir.exists():
        logging.info(f"Creating directory: {filedir}")
        filedir.mkdir(parents=True, exist_ok=True)

    # Créer le fichier s'il n'existe pas
    if not filepath.exists():
        logging.info(f"Creating file: {filepath}")
        filepath.touch()  # Crée un fichier vide
    else:
        logging.info(f"File already exists: {filepath}")
