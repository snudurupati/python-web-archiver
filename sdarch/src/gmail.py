def initgmail(): #initialize connection to gmail and login
	import imaplib, os
	USER = os.environ.get("USER", '')
	PASSWORD = os.environ.get("PASSWORD", '')
	m = imaplib.IMAP4_SSL("imap.gmail.com")
	m.login(USER,PASSWORD)
	m.select(mailbox='Uself')
	return m
    
