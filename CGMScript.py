import os
folder = r'W:\C-130\Pubs\AOU ONLY\NC130CP5GAH471\Graphics\IN-WORK\Rick\CGM'

for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.cgm', '.CGM')
    output = os.rename(infilename, newname)
print("Complete")
