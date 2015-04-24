'''
Updated 12/18/2014 to be resilient to any kind of date format in the gmail search operation.
Module updated on 11/1/2013 to be resilient to any corrected versions of tftds aka multiple emails on same day.'''

#import datetime
from gmail import initgmail

def fetchtml(dtval):
	m = initgmail()
	dt = dtval.strftime('%d %B %Y').lstrip('0') #construct date string of fromat '27 November 2012' and remove any leading 0's as on 01 December.
	#construct a raw search string like '(X-GM-RAW "subject:3 december 2014")'
	rawStr = '(X-GM-RAW "subject:'+dt+'")' 
	resp, msgID = m.search(None, rawStr)
	'''12/18/2014
	resp, msgID = m.search(None,'subject', dt)
	deprecated and replaced with X-GM-RAW search attribute.
	Arguments passed along with the X-GM-RAW attribute when executing the SEARCH or UID SEARCH
	commands will be interpreted in the same manner as in the Gmail web interface.
	if msgID[0]=='':
		resp, msgID = m.search(None, 'subject',dtval.strftime('%d %b %Y').lstrip('0'))
	'''
	items = msgID[0].split() #split, in case more than one email found, corrected versions.
	resp, data = m.fetch(items[len(items)-1], "(RFC822)") #len(items)-1, when more than one email found use the latest, e.g. two emails found fetch items[1]
	tftd = data[0][1]
	typ, msg  = m.fetch(items[len(items)-1], '(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT)])')
	subj = msg[0][1].strip()
	subj = subj.replace('--&--','--and--')
	subj = subj.replace('-&-','--and--')
	subj = subj.replace('--and', '')
	subj = subj.replace('\r', '')
	subj = subj.replace('\n', '')
	subj = subj.split('--')
	indxhdr = subj[1]
	communhdr = subj[2]
	return tftd, indxhdr, communhdr
	m.logout()


