import os
from pathlib import Path

project_name = "us_visa"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",

    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",


    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",

    f"{project_name}/utils/__init__.py", 
    f"{project_name}/utils/main_utils.py", 



    "requirements.txt",
    "setup.py",
    "demo.py"

]
"""
    By placing an __init__.py file in every folder, you are telling Python to treat 
    these directories as packages. This allows you to import your components later 
    using syntax like: from project_name.components import model_trainer.
"""

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File is already present at {filepath}")

"""
Loop Breakdown :-

---------------------------
* filepath = Path(filepath)
* filedir, filename = os.path.split(filepath)

intially the filepath is something like: Bazza/ML-In-Production/__init__.py
it break its into --> 1) filedir = Bazza/ML-In-Production
                      2) filename = __init__.py
---------------------------
* if filedir != "":
*    os.makedirs(filedir, exist_ok=True)

checks if file path is mentioned and if so it os.makedirs makes that folder.
exist_ok checks if it already exist and and prevents the code from crashing.
----------------------------
*if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
*    with open(filepath, w) as f:
*        pass

this code does 2 things, if file doesnt exist then creates it and if it exist but is empty(size=0) then recrease it.
line 2 and 3 are easy way to create an empty file without passing text through it.
----------------------------
"""



