
# why we are creating diffrent scripts for student and teacher ???
#  >>. to maintain the code , to improve understanding of the code
# best practice is to keep diffrent components in diffrent scripts 
# example >> model training and EDa shoule be in diffrent dcript

# Module :: A module is a single file with .py extension that cointains python code 
# inside module function class variable or some code
# ex >> student details.py and teacter_details.py are modules

# package >> colllection of modules organized directories
# each directories can have ,ultiple python scripts 
# example >> student and teacher folder is package which hase 
# versions before python 3.3, to make a package it  was necessary to include>>
# __init__.py in package ( to initialize package and expose required module and function)

# __pycache__ >> known as pyc file >> compiled python files >> source code into byte code >> stored in .pyc file inside __pycache__ directory 
# this helps us to speed up loading the module next time it is imported


# library >> prewritten code to perfrom common task >> collection of multiple package and module
# pandas , numpy 

# importing teacher_details from teacher package

# from teacher import teacher_details # from is used  with package, import is used with modules > generic use from whereever you want to put something from 
import os,sys
# os - provides functionality to interact with operating system
# sys - provides acess to system specific parameters and functions such as python path  The path to script c:\Users\user\Desktop\PWskill\Modules\Module-09 files, EH, MM\pwskills\student\student_details.py
from os.path import dirname , join ,abspath

parent_dir_path = abspath(join(dirname(__file__),".."))
sys.path.insert(0, parent_dir_path)

# at index zero add this directory to the begining of module search/system path 
# it allows to search module and package 

# from teacher import teacher_details
def student():
    print("This is student details")
# teacher_details.teacher() 

# teacher_details.teacher()
# __file__ >> The path to script c:\Users\user\Desktop\PWskill\Modules\Module-09 files, EH, MM\pwskills\student\student_details.py
# dirname >> will give the directory containing the the currrent script 
# The directory of the script c:\Users\user\Desktop\PWskill\Modules\Module-09 files, EH, MM\pwskills\student
# join >> join two oer more path name components , inserting '/' as needed.

# join(dirname(__file__),"..") >> move one directory up  from the current script directory.
# The directory of the script c:\Users\user\Desktop\PWskill\Modules\Module-09 files, EH, MM\pwskills\student\..

# abspath(join(dirname(__file__),"..")) >>  abspath converts the relative path to  absolute path
# The directory of the script c:\Users\user\Desktop\PWskill\Modules\Module-09 files, EH, MM\pwskills
# 