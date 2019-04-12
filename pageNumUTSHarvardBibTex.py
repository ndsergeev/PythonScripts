from tempfile import mkstemp
from shutil import move
from os import fdopen, remove, path
import re
import sys

filePath = ''
filePath2 = ''

p = r'(.*)(pages(=|\s+=|=\s+|\s+=\s+)[{](\s+\d+|\d+)(\s+[-]+|[-]+\s+|[-]+)(\d+|\d+\s+)[}])(.*)'

def simplifyDigits(digits):
    a, b = digits
    a = a.strip()
    b = b.strip()
    if (len(str(a)) == len(str(b))):
        ind = 0
        lst = len(str(b))
        while ind < lst:
            if (str(a)[ind]==str(b)[ind]):
                ind = ind + 1
            else:
                b = str(b)[ind:]
                break
    return 'pages={'+a+'--'+b+'}'

def replace(filePath, filePath2, pattern):
    tmp, absPath = mkstemp()
    with fdopen(tmp,'w') as newFile:
        with open(filePath) as oldFile:
            for line in oldFile:
                finding = re.match(pattern, line)
                if (finding):
                    newFile.write(finding.group(1) +
                                  simplifyDigits([finding.group(4), finding.group(6)]) +
                                  finding.group(7) + "\n")
                else:
                    newFile.write(line)   
    if (filePath2):
        move(absPath, filePath2)
    else:
        move(absPath, filePath)

# Main
if (sys.argv[1]):
    filePath = path.abspath(sys.argv[1])
    if (len(sys.argv) >= 3):
        filePath2 = path.abspath(sys.argv[2])
    replace(filePath, filePath2, p)
        
