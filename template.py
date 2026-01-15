import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "MLProject"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    # create directory if it does not exist
    filedir = filepath.parent
    if filedir != Path("."):
        os.makedirs(filedir, exist_ok=True)

    # create empty file if it does not exist
    if not filepath.exists():
        with open(filepath, "w") as f:
            pass

    logging.info(f"Created: {filepath}")
