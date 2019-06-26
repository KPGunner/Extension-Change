import os
folder = r'Folder Path'

for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.cgm', '.CGM')
    output = os.rename(infilename, newname)
print("Complete")
