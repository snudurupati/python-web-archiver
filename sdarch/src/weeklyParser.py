'''
Weekly lesson overhaul 0f Jan 2018 introduced special characters like:
        =\r
        =3D
        ==
        grep (=[A-Z0-9][A-Z0-9])
'''

import glob, re

cpath = '/Users/snudurupati/Documents/sdarch/C'
files = glob.glob1(cpath+"/raw", "*.html")

def parseweekly(fpath, filename):

    sfile = open(fpath+"/raw/"+filename, 'rt')
    tfile = open(fpath+"/"+filename, 'w')

    html = sfile.read()
    html = html.replace('=\n','')
    html = html.replace('3D','')
    #html = html.replace('==','')
    html = re.sub('(=[A-Z0-9][A-Z0-9])', '', html)     #regex to replace pattern: =[letter or number][letter or number]  --> (=[A-Z0-9][A-Z0-9])
    html = html.replace('Sri Gaura Hari das at raghav.sreeram@gmail.com', 'you')
    html = html.replace('This request was made on: November 30, 2012', '')
    html = html.replace('From the', '')
    html = html.replace('following IP address:', '')
    html = html.replace('96.61.241.6', '')

    tfile.write(html)
    sfile.close()
    tfile.close()


for filename in files:
    print filename
    parseweekly(cpath, filename)

