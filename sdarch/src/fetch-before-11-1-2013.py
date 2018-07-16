import datetime
from gmail import initgmail

def fetchtml(dtval):
	m = initgmail()
	dt = dtval.strftime('%d %B %Y') #construct date string of fromat '27 November 2012'
	dt = dt.lstrip('0') #remove any leading 0's as on 01 December.
	resp, items = m.search(None,'subject', dt) # Search email subject for a string like '27 November 2012'
	items = items[0].split()
	resp, data = m.fetch(items[0], "(RFC822)")
	tftd = data[0][1]
	typ, msg  = m.fetch(items[0], '(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT)])')
	subj = msg[0][1].strip()
	subj = subj.replace('--and', '')
	subj = subj.split('--')
	indxhdr = subj[1]
	communhdr = subj[2]
	return tftd, indxhdr, communhdr
  
    
