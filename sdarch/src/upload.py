import ftplib, os

def upfile(dtval,fname, fob):
	FTPUSER = os.environ.get("FTPUSER", '')
	FTPPASS = os.environ.get("FTPPASS", '')
	ftps = ftplib.FTP('www.sda-archives.com', FTPUSER, FTPPASS)
	#ftps.prot_p()
	mth = dtval.strftime('%b').lower()
	year = dtval.strftime('%Y')
	path = '/tftd/tftd/'+year+'/'+mth
	ftps.cwd(path)
	ftps.storlines('STOR '+fname, fob)
	ftps.quit()

	

def upimg(imgname, fob, ftps):
	path = '/picture_library'
	ftps.cwd(path)
	ftps.storbinary('STOR '+imgname, fob)
	ftps.quit()

