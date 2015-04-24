''' Module updated on 11/1/2013 to be resilient to any corrected versions of tftds aka multiple emails on same day.'''

#import datetime
from gmail import initgmail

def fetchtml(dtval):
	m = initgmail()
	dt = dtval.strftime('%d %B %Y') #construct date string of fromat '27 November 2012'
	dt = dt.lstrip('0') #remove any leading 0's as on 01 December.
	resp, msgID = m.search(None,'subject', dt)
	if msgID[0]=='':
		resp, msgID = m.search(None, 'subject',dtval.strftime('%d %b %Y').lstrip('0'))
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


