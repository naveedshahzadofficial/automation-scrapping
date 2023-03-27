# automation-scrapping

### To Freeze the requirements:
pip freeze > requirements.txt

### To install the requirements:
pip install -r requirements.txt

### Environment Setup
python -m venv env
###### for specific path
python -m venv /path/to/new/virtual/environment
###### for activate on Linux/Mac
source env/bin/activate 
###### for activate on Windows
env\Scripts\activate 

###### if you have already added the directory to your Git repository
git rm -r --cached env