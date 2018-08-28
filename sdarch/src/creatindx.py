import upload


def indxhtml(dtval, indxhdr, ftps):
	dd = dtval.strftime('%d')
	mm = dtval.strftime('%m')
	month = dtval.strftime('%b')
	yy = dtval.strftime('%y')
	f1 = open('tftd/index.html','r')
	html = f1.read()
	f1.close()
	title = ' Daily Thoughts | '+dtval.strftime('%B %Y')
	html = html.replace(' Daily Thoughts | June 2012 ',title)
	html = html.replace('June', month)
	if dd == '31':
		html = html.replace('<!--'+month+' 31:-->',month+' 31:')
		srclnk = '<!--a href="tftd_063112.html"-->&nbsp;'
		replnk = '<a href="tftd_'+mm+dd+yy+'.html">'+indxhdr
		#print srclnk, "\\n", replnk
		html = html.replace(srclnk, replnk)
	else:
		srclnk = '"tftd_06'+dd+'12.html">&nbsp;'
		replnk = '"tftd_'+mm+dd+yy+'.html">'+indxhdr
		html = html.replace(srclnk, replnk)
	f2 = open('tftd/index.html','w')
	f2.write(html)
	f2.close()
	f2 = open('tftd/index.html','r')
	upload.upfile(dtval,'index.html',f2, ftps)
	f2.close()



def communhtml(dtval, communhdr, ftps):
	dd = dtval.strftime('%d')
	mm = dtval.strftime('%m')
	month = dtval.strftime('%b')
	yy = dtval.strftime('%y')
	f1 = open('tftd/commun.html','r')
	html = f1.read()
	f1.close()
	title = ' Communications | '+dtval.strftime('%B %Y')
	html = html.replace(' Communications | June 2012 ',title)
	html = html.replace('June', month)
	if dd == '31':
		html = html.replace('<!--'+month+' 31:-->',month+' 31:')
		srclnk = '<!--a href="tftd_063112.html#W"-->&nbsp;'
		replnk = '<a href="tftd_'+mm+dd+yy+'.html#W">'+communhdr
		#print srclnk, "\\n", replnk
		html = html.replace(srclnk, replnk)
	else:
		srclnk = '"tftd_06'+dd+'12.html#W">&nbsp;'
		replnk = '"tftd_'+mm+dd+yy+'.html#W">'+communhdr
		#print srclnk, replnk
		html = html.replace(srclnk, replnk)
	f2 = open('tftd/commun.html','w')
	f2.write(html)
	f2.close()
	f2 = open('tftd/commun.html','r')
	upload.upfile(dtval,'commun.html',f2, ftps)
	f2.close()
