import os
import shutil
from datetime import datetime 
import textwrap

a=datetime.today().date().strftime("%m_%d_%Y")
print(a)

source_path = "//global.ecolab.corp/apac/IN-Pune/GROUPS/Planning_Analytics/Projects/Plan Capture Data/JDA_SKUPROJ_02_21_2022.csv"
dest_path = "https://ecolab.sharepoint.com/:f:/r/sites/scplanninganalytics/Shared%20Documents/Projects%20-%20Pune/Plan%20Capture%20Database/Data%20Repository?csf=1&web=1&e=g7XgsS"

shutil.copy(source_path,dest_path)





