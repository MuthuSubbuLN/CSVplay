#!/bin/python

import pandas as pd
import glob as glob

header_names = ['SN1', 'Name1', 'Cont1']

path = r'csvfiles/' # use your path
all_files = glob.glob(path + "*.csv")
new_path = glob.glob(r'csvfiles1/')

for filename in all_files:
    print('\n source path : ' , filename)
    # pp = r'csvfiles1/{filename.split('/')[-1]}'
    pp = "{}/{}".format("csvfiles1", filename[1])
    print('destination path : ' , pp)
    df = pd.read_csv(filename, header=None,skiprows=1,names=header_names)
    df.to_csv(pp, index = False, header=True)

print('£££ modified files exported to new location! \n')

print('==> read files from destination path <== \n')

files = glob.glob(r"csvfiles1/*.csv")

for destFile in files:
    print('\n log1', pd.read_csv(destFile, sep=";"))
    
