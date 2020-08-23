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
    df = pd.read_csv(filename, header=None,skiprows=1,names=header_names)
    print('source path : ', filename)
    file = filename.split('/')
    pp = "{}/{}".format("csvfiles1", file[1])
    print('destination path : ', pp)
    df.to_csv(pp, index = False, header=True)
    print('\n')

print('£££ modified files exported to new location! \n')

print('==> read files from destination path <==')

destinationPath = r'csvfiles1/'
files = glob.glob(destinationPath + "*.csv")
print('\n')
for destFile in files:
    dfs = pd.read_csv(destFile, sep=";")
    print('log1 ')
    print(dfs)
    print('\n')
