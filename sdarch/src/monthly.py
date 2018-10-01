#Creates a directory for each new month on archives site via FTP
import ftplib
import datetime, os

dtval = datetime.date.today()
#initialize ftp connection
FTPUSER = os.environ.get("FTPUSER", '')
FTPPASS = os.environ.get("FTPPASS", '')
ftps = ftplib.FTP('www.sda-archives.com', FTPUSER, FTPPASS)
print ftps
mth = dtval.strftime('%b').lower()
year = dtval.strftime('%Y')
path = '/tftd/tftd/'+year+'/'+mth
print path
ftps.mkd(path)
ftps.quit()
