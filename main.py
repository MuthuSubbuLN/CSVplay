import csv
import pandas as pd
import glob as glob

with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])

#
# df = pd.read_csv (glob.glob('csvfiles/*.csv'))
# print (df)
# # df.to_csv('csvfiles2/f1.csv')
# df.head()
# header_names = ['SN1', 'Name1', 'Cont1']
# df = pd.read_csv ('csvfiles/file1.csv',header=None,skiprows=1,names=header_names)
# df.head()
# print('ada ' )
# print(df)
# df.to_csv(r'csvfiles1/file1.csv', index = False, header=True)
header_names = ['SN1', 'Name1', 'Cont1']
print('export done!')

path = r'csvfiles/' # use your path
all_files = glob.glob(path + "*.csv")
new_path = glob.glob(r'csvfiles1/')

for filename in all_files:
    df = pd.read_csv(filename, header=None,skiprows=1,names=header_names)
    print(filename)
    file = filename.split('/')
    # new_path1 = glob.glob(r'csvfiles1/' + file[1])
    pp = "{}/{}".format("csvfiles1", file[1])
    print('log1 ', df)
    print('\n')
    df.to_csv(pp, index = False, header=True)

print('all files export done!')