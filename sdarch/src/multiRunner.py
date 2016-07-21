__author__ = 'snudurupati'
import fetchNoIdx
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

# this will give you a list containing all the dates
dd = [begin + timedelta(days=x) for x in range((end - begin).days + 1)]

def mainfunc(dtval):
    #print dtval
    tftd, indxhdr, communhdr = fetchNoIdx.fetchtml(dtval)
    html = parse.parsetml(tftd, dtval.strftime('%B'))
    urlist, namlist = getfile.geturl(html)
    getfile.getimg(urlist,namlist)
    html = parse.replimgsrc(html)
    fpath = dtval.strftime('tftd/tftd_%m%d%y.html')
    #fname = dtval.strftime('tftd_%m%d%y.html')
    f=open(fpath,'w')
    f.write(html)
    f.close()
    f=open(fpath,'r')
    #upload.upfile(dtval,fname,f)
    f.close()
    lindxhtml(dtval, indxhdr)
    lcommunhtml(dtval, communhdr)

for dt in dd:
    mainfunc(dt)