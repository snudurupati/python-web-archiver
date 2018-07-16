# parsetml cleans up the tftd html from the email and attches tftd_template headers and footers.

def parsetml(tftd, mth):
    loc1 = tftd.find('#183C5B">')
    #loc1 = tftd.find('</head>')
    loc2 = tftd.find('</body>')
    html = tftd[loc1+9:loc2]
    #html = tftd[loc1+7:loc2]
    loc3 = html.find('<TABLE ID="aweber_rem"')
    loc4 = html.find('</body>')
    html = html.replace(html[loc3:loc4], '')
    loc5 = html.find('Our records indicate')
    loc6 = html.find('96.61.241.6')
    html = html.replace(html[loc5:loc6+11], '')
    html = html.replace('{contact_address', '')
    html = html.replace('The Ultimate Self Realization Course<br>','')
    html = html.replace('Post Office Box 143073<br>','')
    html = html.replace('Austin, Texas 78714-3072<br>','')
    html = html.replace('United States of America','')
    html = html.replace('Unsubscribe','')
    html = html.replace('Change Subscriber Options','')
    html = html.replace('Answers by Citing the Vedic Version:','<a name="W"></a>Answers by Citing the Vedic Version:')
    hdr  = "<html xmlns='http://www.w3.org/1999/xhtml'><body><div align='center'>  <p class='ct'><a href='../../../index.html'>Back to Home Page</a></p><p class='ct'><a href='index.html'>Back to "+mth+" </a><a href='index.html'> Index</a></p><br /></div>"
    fotr = "<p align=center><a href='../../../index.html'>Back to Home Page</a></p><p align=center><a href='index.html'>Back to "+mth+" Index</a></p></body></html>"
    html = hdr+html+fotr
    return html

# replimgsrc replaces all image src's pointing to www.backtohome.com to a relative path of /picture_library.

def replimgsrc(html):
    #html = html.replace('<img border="0" src="http://www.backtohome.com/images','<img border="0" /picture_library')
    #html = html.replace('<img border="3" src="http://www.backtohome.com/images','<img border="0" src="/picture_library')
    i=1
    while i <len(html):
	loc1 = html.find('src',i)
	loc2 = html.find(' ', loc1)
	i = loc2
	if i == -1:
		break
	#print 'src="/picture_library'+html[loc1:loc2].split('/')[-1]
        html = html.replace(html[loc1:loc2],'src="/picture_library/'+html[loc1:loc2].split('/')[-1])
    return html
