import os
from os.path import getsize


dir = ('safebrowsing')
filenames = []
for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)) and 'mozstd-trackwhite' in file: # noqa
            size = os.path.getsize(os.path.join(dir, file))
            if size <= 200000:
                assertTrue size <= 200000
                filenames.append(file)
            else:
                print file + (' is over maximum filesize')
print filenames
print (' are under maximum filesize')
