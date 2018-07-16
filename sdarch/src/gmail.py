def initgmail(): #initialize connection to gmail and login
	import imaplib
	m = imaplib.IMAP4_SSL("imap.gmail.com")
	m.login('raghavsreeram','Spark4DS!')
	m.select(mailbox='Uself')
	return m
    
