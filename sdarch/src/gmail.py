def initgmail(): #initialize connection to gmail and login
	import imaplib
	m = imaplib.IMAP4_SSL("imap.gmail.com")
	m.login('raghavsreeram','iloveindia1X')
	m.select(mailbox='Uself')
	return m
    
