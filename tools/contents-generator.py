import os
import sys


# get file name from args and check if it exists
fp = sys.argv[1]
print(fp)
if os.path.exists(fp):
    print(os.path.basename(fp))
else:
    raise Exception(f'{fp} does not exist')

with open(fp) as f:
    headers = []
    for line in f.readlines():
        if('#' in line and 'contents' not in line.lower() and '[[' not in line):
            headers.append({
                'headerCount': line.count('#')-1,
                'name': line.split('# ')[1].strip()
            })
    
    for header in headers:
        tabs = ""
        for i in range(header['headerCount']):
            tabs += "\t"
        
        print(f'{tabs}- [{header["name"]}](#{header["name"]})')
    