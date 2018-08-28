# parsetml cleans up the tftd html from the email and attaches tftd_template headers and footers.

def parsetml(tftd, mth):
    import re
    loc1 = tftd.find('<head>') #updated to not get email headers from gmail fetches.
    loc2 = tftd.find('</body>')
    html = tftd[loc1:loc2]

    '''TFTD overhaul 0f Jan 2018 introduced special characters like:
        =\r
        3D
        ==
        grep (=[A-Z0-9][A-Z0-9])
        '''

    #8-8-2018 Start

    html = html.replace('=\r\n','')
    #html = html.replace('=\r\n','')
    #html = html.replace('=E2=80=8B','') #this is just redundant after above regex replacer
    html = html.replace('3D','')
    #html = html.replace('=09','')
    #html = html.replace('=20','')
    html = html.replace('==','')
    #html = html.replace('=E2=80=8B','')
    html = html.replace('&nbsp;',' ')
    html = html.replace('|',' ')
    #8-8-2018 End

    #regex to replace pattern: =[letter or number][letter or number]  --> (=[A-Z0-9][A-Z0-9])
    html = re.sub('(=[A-Z0-9][A-Z0-9])', '', html)

    html = html.replace('Answers According to Vedic Wisdom','<a name="W"></a>Answers According to Vedic Wisdom')
    html = html.replace('Our records indicate that Sri Gaura Hari das at raghav.sreeram@gmail.com requested to be enrolled to receive e-mails from the Ultimate Self Realization Course at: http://backtohome.com/', '')
    html = html.replace('This request was made on: November 30, 2012 From the following IP address: 96.61.241.6 {contact_address}', '')
    html = html.replace('Unsubscribe', '')
    html = html.replace('Change Subscriber Options', '')

    hdr = """<html xmlns:v="urn:schemas-microsoft-com:vml">"""
    fotr = "<p align=center><a href='../../index.html'>Back to Home Page</a></p><p align=center><a href='index.html'>Back to "+mth+" Index</a></p></body></html>"
    html = hdr+html+fotr

    return html

def replimgsrc(html):
    #html = html.replace('<img border="0" src="http://www.backtohome.com/images','<img border="0" /picture_library')
    html = html.replace('<img border="3" src="http://www.backtohome.com/images','<img border="0" src="/picture_library')
    i=1
    while i <len(html):
	loc1 = html.find('src=',i)
	loc2 = html.find(' ', loc1)
	i = loc2
	if i == -1:
		break
	#print 'src="/picture_library'+html[loc1:loc2].split('/')[-1]
        #print html[loc1:loc2], len(html)
        html = html.replace(html[loc1:loc2],'src="/picture_library/'+html[loc1:loc2].split('/')[-1])
        #print html
    return html
