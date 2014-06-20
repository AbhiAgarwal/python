# This will take a URL/.txt file, take all the emails out of it and check if they are valid.
# the regular expression library
import re
# Natural Language Toolkit - symbolic and statistical natural language processing.
import nltk
# opens file objects from the Web by accessing them via their URL (Hence urlopen library)
from urllib import urlopen

true_emails = []
false_emails = []

def main():
	# url that you want to retrieve all the emails from
	url = "http://www.419baiter.com/_scam_emails/scammer-email-addresses.html"
	# opens URL and stores it into HTML
	# or html = open('file.txt')
	html = urlopen(url).read()
	# puts the HTML syntax into str
	str = nltk.clean_html(html)
	# sample emails:
	# str is the emails: this can be anything from an HTML document to a simple string
	# a@a.gn is the shortest domain, or n.dk is a real domain
	# empty string at first but then gets populated
	strToSearch = ""
	# takes all the stuff from str (website, ect.) and populates it into strToSearch
	for line in str:
		strToSearch += line
	# checks to find all the emails printed within strToSearch
	email_pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+") # regular expression
	emails = re.findall(email_pattern, strToSearch)
	testEmails(emails)
	numberofEmailURL(emails, url)
	# numberofEmail(emails) # for if you input string for URL

# function to validate the emails to check if they are true
def validateEmail(emails): # Largest email length is 254: http://www.rfc-editor.org/errata_search.php?rfc=3696&eid=1690
	if len(emails) > 5 and len(emails) < 254: # checking length of email to be greater than 5 (a@a.gn name is 6 in length)
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", emails) != None:
			return 1 # smallest domain could be k@k.st
	return 0

def numberofEmailURL(emails, url):
	print "There are " + str(len(emails)) + " emails in the URL: " + url

def numberofEmail(emails):
	print "There are " + str(len(emails)) + " emails."

def numberofFalseEmails():
	print "There are " + str(len(false_emails)) + " fake emails."

# will print all the emails that are valid/invalid in the strlist
def testEmails(emails):
	for i in emails:
		returns = validateEmail(i)
		if (returns == 1):
			true_emails.append(i)
		else:
			false_emails.append(i)

if __name__ == '__main__':
    main()
