__author__ = 'snudurupati'
import fetch
import parse
import getfile
from creatindx import indxhtml, communhtml
import upload
import os, sys
from datetime import date, timedelta
import calendar

os.chdir(os.path.dirname(os.path.abspath(__file__)))
yr = int(sys.argv[1])
mnth = int(sys.argv[2])
fday, numdays = calendar.monthrange(yr, mnth)
begin = date(yr, mnth, 1)
end = date(yr, mnth, numdays)

# this will give you a list containing all of the dates
dd = [begin + timedelta(days=x) for x in range((end - begin).days + 1)]

os.system("mv tftd tftd_$(date +%m%Y)_bkp")
os.system("mkdir tftd")
os.system("cp template/* tftd")

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
    upload.upfile(dtval,fname,f)
    indxhtml(dtval, indxhdr)
    communhtml(dtval, communhdr)
    f.close()

for dt in dd:
    mainfunc(dt)