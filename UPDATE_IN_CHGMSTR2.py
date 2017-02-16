import csv
import os
import re

path = os.path.normpath("C:\\Users\\BaylorB\\Google Drive\\Integris_EPIC")
listFile = os.path.join(path, "IN_CHGMSTR.txt")
updatefile = os.path.join(path, "UPDATE_CHGMSTR.txt")

print(listFile)

left = 'left', 'LEFT', 'lt', 'LT'
right = 'right', 'RIGHT', 'rt', 'RT'
bilat = 'BILATERAL', 'bilateral', 'Bilat', 'BILAT'

words = ['left', 'LEFT', 'lt', 'LT','right', 'RIGHT', 'rt', 'RT''BILATERAL', 'bilateral', 'Bilat', 'BILAT']

def main():
    p = open(updatefile, 'w')
    with open(listFile, 'r+') as f:
        
        reader = csv.reader(f, delimiter = '\t')
        writer = csv.writer(p, delimiter = '\t')

        for a in reader:
            if 'LEFT' in a[3]:
                a[1] = 'LT'
                writer.writerow(a)
            elif 'left' in a[3]:
                a[1] = 'LT'
                writer.writerow(a)
            elif 'lt' in a[3]:
                a[1] = 'LT'
                writer.writerow(a)
            elif 'LT' in a[3]:
                a[1] = 'LT'
                writer.writerow(a)
            elif 'right' in a[3]:
                a[1] = 'RT'
                writer.writerow(a)
            elif 'RIGHT' in a[3]:
                a[1] = 'RT'
                writer.writerow(a)
            elif 'rt' in a[3]:
                a[1] = 'RT'
                writer.writerow(a)
            elif 'RT' in a[3]:
                a[1] = 'RT'
                writer.writerow(a)
            elif 'BILATERAL' in a[3]:
                a[1] = '50'
                writer.writerow(a)
            elif 'bilateral' in a[3]:
                a[1] = '50'
                writer.writerow(a)
            elif 'Bilat' in a[3]:
                a[1] = '50'
                writer.writerow(a)
            elif 'BILAT' in a[3]:
                a[1] = '50'
                writer.writerow(a)

            writer.writerow(a)

    p.close()
if __name__ == "__main__":
      # execute only if run as a script
      main()
