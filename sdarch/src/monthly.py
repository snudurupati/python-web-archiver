#Creates a directory for each new month on archives site via FTP
import ftplib
import datetime

dtval = datetime.date.today()
ftps = ftplib.FTP('www.sda-archives.com','gaurahari','Bhagavan108')
mth = dtval.strftime('%b').lower()
year = dtval.strftime('%Y')
path = '/tftd/tftd/'+year+'/'+mth
#print path
ftps.mkd(path)
ftps.quit()
