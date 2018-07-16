#import initsdarch
import fetch
import datetime
import parse
import getfile
from creatindx import indxhtml, communhtml
import upload
import logging
import logging.handlers
import sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

dtval = datetime.date.today()
SUB = dtval.strftime('Sdarch Error - %d %B %Y')
#print SUB
smtp_handler = logging.handlers.SMTPHandler(mailhost=("smtp.gmail.com", 587), #port 578 for TLS
                                            fromaddr="raghav.sreeram@gmail.com",
                                            toaddrs="raghav.sreeram@gmail.com",
                                            subject=SUB,
                                            credentials=('raghav.sreeram','iloveindia1X'),
                                            secure=()) #secure with empty tupule uses STARTTls

logger = logging.getLogger()
logger.addHandler(smtp_handler)

def mainf():
    dtval = datetime.date.today()
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
    return

try:
    mainf()

except Exception as e:
  logger.error(e)












