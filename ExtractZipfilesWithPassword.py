import os, zipfile, sys

def ExtractZipfiles(sourceDir, destinationDir):

  for filename in os.listdir(sourceDir):
    print filename
    with zipfile.Zipfile(os.path.join(sourceDir, filename)) as zf:
      name = zf.namelist()
      print name
      zf.extractall(destinationDir, name, 'password')
      
ExtractZipfiles(sys.argv[1], sys.argv[2])
