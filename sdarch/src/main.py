import fetchNoIdx
import datetime
import parse
import getfile
from creatindx import indxhtml, communhtml
import upload
import os, sys
#sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#print int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
dtval = datetime.date(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
#dtval = datetime.date(2018,8,28)
tftd, indxhdr, communhdr = fetchNoIdx.fetchtml(dtval)
html = parse.parsetml(tftd, dtval.strftime('%B'))
#print html
urlist, namlist = getfile.geturl(html)
getfile.getimg_ftp(urlist,namlist) #uploads images to ftp site
html = parse.replimgsrc(html)
fpath = dtval.strftime('tftd/tftd_%m%d%y.html')
fname = dtval.strftime('tftd_%m%d%y.html')
f=open(fpath,'w')
f.write(html)
f.close()
f=open(fpath,'r')
upload.upfile(dtval,fname,f)
#updae and upload index files.
indxhtml(dtval, indxhdr)
communhtml(dtval, communhdr)
f.close()







