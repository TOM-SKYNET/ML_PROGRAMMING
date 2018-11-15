import sys, os
for path, subdirs, files in os.walk('/Users/krista/Desktop/TOM/AI/LAB/Python'):
    for name in files:
        print os.path.join(path, name)
    print subdirs
    print 'path ',path