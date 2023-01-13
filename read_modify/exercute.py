import os
import datetime

import pdflatex
import all_functions as af

# Current Directory
current_path=os.getcwd()
folder='TEMPLATE_CFC'
current_folder_path=os.path.join(current_path,folder)

#Input Dictionary
today=datetime.date.today()
Dict={'-VAR1-': 10000000, '-VAR2-': 999, '-PROJECTNAME-': 'CEBU 1234567', '-DATE-': str(today)}


# Single latex
# Single Dict

file_name='EngCalcPaper_CFC.tex'

file=os.path.join(current_folder_path,file_name)

af.single_latex_single_dict(file, Dict)









