from pdfrw import PdfReader, PdfWriter, PageMerge
import sys
import os

argv = sys.argv[1:]
file1name, file2name  = argv
outputFilename = 'overlay.' + os.path.basename(file1name)

file1 = PdfReader(file1name)
file2 = PdfReader(file2name)
# 2nd option: check both file's pagecount and swap them so the bigger is first(?)

i = 0
try:
    for page in file2.pages:
        PageMerge(page).add(file1.pages[i]).render()
        i += 1
except IndexError:
    print("Error: files have unequal pagecount")
    print("Stopping.")
    exit(1)

PdfWriter(outputFilename, trailer=file2).write()