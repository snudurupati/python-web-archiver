def initgmail(): #initialize connection to gmail and login
	import imaplib
	m = imaplib.IMAP4_SSL("imap.gmail.com")
	m.login('raghavsreeram','maskedpass')
	m.select(mailbox='Uself')
	return m
    
