#!/bin/python

import pandas as pd
import glob as glob

# import csv 
# Create CSV files
# with open('innovators.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Name", "Contribution"])
#     writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
#     writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
#     writer.writerow([3, "Guido van Rossum", "Python Programming"])

header_names = ['SN1', 'Name1', 'Cont1']

path = r'csvfiles/' # use your path
all_files = glob.glob(path + "*.csv")
new_path = glob.glob(r'csvfiles1/')

for filename in all_files:
    print('\n source path : {filename}')
    print('destination path : csvfiles1/{filename.split('/')[1]}')
    df = pd.read_csv(filename, header=None,skiprows=1,names=header_names)
    df.to_csv(pp, index = False, header=True)

print('£££ modified files exported to new location! \n')

print('==> read files from destination path <== \n')

files = glob.glob(r'csvfiles1/*.csv")

for destFile in files:
    print('\n log1', pd.read_csv(destFile, sep=";"))
    
