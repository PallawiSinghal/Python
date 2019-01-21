import shutil
import os
src = "subfolder/dir_031/"
destination = "/backgrouund_all_in_one/"
def move(src, dest):
    shutil.move(src, dest)
count = 0
for dirpath, dirs, files in os.walk(src):
    for filesname in files:
    	count = count + 1
    	
    	old = dirpath + "/" + filesname
    	new = destination  + "atm_" + str(count) + ".jpeg"
    	print (new)
    	move(old, new)
    	
