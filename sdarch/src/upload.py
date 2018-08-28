import ftplib, os

def upfile(dtval,fname, fob, ftps):
	mth = dtval.strftime('%b').lower()
	year = dtval.strftime('%Y')
	path = '/tftd/tftd/'+year+'/'+mth
	ftps.cwd(path)
	ftps.storlines('STOR '+fname, fob)


def upimg(imgname, fob, ftps):
	path = '/picture_library'
	ftps.cwd(path)
	ftps.storbinary('STOR '+imgname, fob)

