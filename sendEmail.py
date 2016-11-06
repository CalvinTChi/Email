import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.mime.application
import getopt, sys

def main(argv):
	global account
	global password
	global sender
	global subject
	global attachments
	global bodycontent
	attachments = None
	addresses = None
	names = None
	specs = None
	body = None
	try:
		# i.e. "i:" means that argument for i is required
		opts, args = getopt.getopt(argv, "s:b:")
	except getopt.GetoptError:
		print("Usage: sendEmail.py -s <specifications> -b <body>")
		# Exit status of 2 means command line synax error
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-s":
			specs = arg
		elif opt == "-b":
			body = arg
	with open(body, "r") as myBody:
		bodycontent = myBody.read()
	specscontent = [row.strip() for row in open(specs)]
	for line in specscontent:
		items = line.split("=")
		if items[0] == "addresses":
			addresses = list(items[1].split(","))
		elif items[0] == "account":
			account = items[1]
		elif items[0] == "password":
			password = items[1]
		elif items[0] == "sender":
			sender = items[1]
		elif items[0] == "subject":
			subject = items[1]
		elif items[0] == "attachments" and len(items[1]) > 1:
			attachments = list(items[1].split(","))
		elif items[0] == "recepients":
			names = list(items[1].split(","))
	if not addresses or not account or not password or not sender or not subject or not names:
		print("Make sure field names for 'account', 'password', 'sender', 'addresses', 'subject', and 'recepients' are filled")
		sys.exit(1)
	if len(addresses) != len(names):
		print("Make sure you have as many recepient names as addresses")
		sys.exit(1)
	i = 0
	for address, name in zip(addresses, names):
		print("Sending email to %s..." % name)
		send(address, name)
		i += 1
	print("%d emails sent!" % i)

def send(address, name):
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = address
	text = bodycontent % name
	msg.attach(MIMEText(text, 'plain'))

	# Attach documents
	if attachments:
		for attachment in attachments:
			f = open(attachment, 'rb')
			att = email.mime.application.MIMEApplication(f.read())
			f.close()
			att.add_header('Content-Disposition','attachment',filename=attachment)
			msg.attach(att)

	# Send mail
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(account, "#NewEra8")
	s.sendmail(account, address, msg.as_string())
	s.quit()

if __name__ == "__main__":
	try:
		arg1 = sys.argv[1]
		arg2 = sys.argv[2]
	except:
		print("Usage: sendEmail.py -s <specifications> -b <body>")
		sys.exit(2)
	main(sys.argv[1:])



