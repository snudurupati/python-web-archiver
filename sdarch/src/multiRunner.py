__author__ = 'snudurupati'
import fetch
import parse
import getfile
from lcreatindx import lindxhtml, lcommunhtml
import os, sys
from datetime import date, timedelta

os.chdir(os.path.dirname(os.path.abspath(__file__)))
yr = int(sys.argv[1])
mnth = int(sys.argv[2])
#fday, numdays = calendar.monthrange(yr, mnth)
fday = int(sys.argv[3])
lday = int(sys.argv[4])
begin = date(yr, mnth, fday)
end = date(yr, mnth, lday)

# this will give you a list containing all of the dates
dd = [begin + timedelta(days=x) for x in range((end - begin).days + 1)]

'''os.system("mv tftd tftd_$(date +%m%Y)_bkp")
os.system("mkdir tftd")
os.system("cp template/* tftd")'''

def mainfunc(dtval):
    #print dtval
    tftd, indxhdr, communhdr = fetch.fetchtml(dtval)
    html = parse.parsetml(tftd, dtval.strftime('%B'))
    urlist, namlist = getfile.geturl(html)
    getfile.getimg(urlist,namlist)
    html = parse.replimgsrc(html)
    fpath = dtval.strftime('tftd/tftd_%m%d%y.html')
    fname = dtval.strftime('tftd_%m%d%y.html')
    f=open(fpath,'w')
    f.write(html)
    f.close()
    f=open(fpath,'r')
    #upload.upfile(dtval,fname,f)
    lindxhtml(dtval, indxhdr)
    lcommunhtml(dtval, communhdr)
    f.close()

for dt in dd:
    mainfunc(dt)