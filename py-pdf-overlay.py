from pdfrw import PdfReader, PdfWriter, PageMerge
import sys, os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('file1')
parser.add_argument('file2')
parser.add_argument('-o', dest='output', metavar='output', help='save overlayed pdf there, default is "overlay.<file1>.pdf"')

parsed = parser.parse_args()

try:
    file1 = PdfReader(parsed.file1)
    file2 = PdfReader(parsed.file2)
except:
    print("Error: specified file doesn't exist.")
    print("Stopping")
    exit(1)
outputFilename = parsed.output or f'overlay.{os.path.basename(parsed.file1)}'

i = 0
try:
    for page in file2.pages:
        PageMerge(page).add(file1.pages[i]).render()
        i += 1
except IndexError:
    print("Error: files have unequal pagecount")
    print("Stopping.")
    exit(1)
except:
    print("Error parsing the file")
    print("Stopping.")
    exit(1)

PdfWriter(outputFilename, trailer=file2).write()
print(f'Successfully merged into "{outputFilename}"')
