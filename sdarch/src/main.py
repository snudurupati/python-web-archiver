import datetime, ftplib
import os, sys
import fetchNoIdx, parse
import getfile, upload
from creatindx import indxhtml, communhtml

#sys.path.append(os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#print int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
dtval = datetime.date(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))

#initialize ftp connection
FTPUSER = os.environ.get("FTPUSER", '')
FTPPASS = os.environ.get("FTPPASS", '')
ftps = ftplib.FTP('www.sda-archives.com', FTPUSER, FTPPASS)

tftd, indxhdr, communhdr = fetchNoIdx.fetchtml(dtval)
html = parse.parsetml(tftd, dtval.strftime('%B'))
#print html
urlist, namlist = getfile.geturl(html)
getfile.getimg(urlist,namlist, ftps) #uploads images to ftp site
html = parse.replimgsrc(html)
fpath = dtval.strftime('tftd/tftd_%m%d%y.html')
fname = dtval.strftime('tftd_%m%d%y.html')
f=open(fpath,'w')
f.write(html)
f.close()
f=open(fpath,'r')
upload.upfile(dtval,fname,f,ftps)

#updae and upload index files.
indxhtml(dtval, indxhdr, ftps)
communhtml(dtval, communhdr, ftps)
f.close()
ftps.quit()







