import getopt
import os

import sys

import shutil

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

print "Bat2Exe v0.1, Created By SilicaAndPina."
path = raw_input("Location of .bat file: ")
icon = raw_input("Location of icon file (optional): ")
console = raw_input("Show Console? [y/n]: ")
admin = raw_input("Run As Administrator [y/n]: ")
global fconsole,fadmin,ficon
if console == "y":
    fconsole = ""
elif console == "n":
    fconsole = " -w "
if admin == "y":
    fadmin = " --uac-admin "
elif admin == "n":
    fadmin = ""

if icon != "":
    ficon = " -i "+icon
elif icon == "":
    ficon = ""

with open(path, 'r') as src:
    with open(path+'.py', 'w') as dest:
       dest.write('import os\n')
       for line in src:
           dest.write('%s%s%s\n' % ('os.system("', line.rstrip('\n'), '")'))

os.system("C:\Python27\Scripts\pyinstaller.exe"+ficon+fconsole+fadmin+" "+path+".py")
os.remove(path+".py")
shutil.rmtree(path+"build")
os.remove(path+".spec")
print ('Done!!')


