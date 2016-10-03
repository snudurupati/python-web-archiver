import ftplib
import datetime

def upfile(dtval,fname, fob):
	
	#ftps = ftplib.FTP_TLS('www.sda-archives.com','gaurahari','Bhagavan108') #FTP_TLS stopped working on 2/9/2013
	ftps = ftplib.FTP('www.sda-archives.com','gaurahari','Bhagavan108')
	#ftps.prot_p()
	mth = dtval.strftime('%b').lower()
	year = dtval.strftime('%Y')
	path = '/tftd/tftd/'+year+'/'+mth
	ftps.cwd(path)
	ftps.storlines('STOR '+fname, fob)
	ftps.quit()

	
def upimg(imgname, fob):
    #ftps = ftplib.FTP_TLS('www.sda-archives.com','gaurahari','Bhagavan108')
    ftps = ftplib.FTP('www.sda-archives.com','gaurahari','Bhagavan108')
    #ftps.prot_p()
    path = '/picture_library'
    ftps.cwd(path)
    ftps.storbinary('STOR '+imgname, fob)
    ftps.quit()

