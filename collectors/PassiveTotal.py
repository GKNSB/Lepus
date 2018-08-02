import requests
from termcolor import colored
from ConfigParser import SafeConfigParser


def init(domain):
	PT = []

	print colored("[*]-Searching PassiveTotal...", 'yellow')

	parser = SafeConfigParser()
	parser.read('config.ini')
	PT_KEY = parser.get('PassiveTotal', 'PT_KEY')
	PT_SECRET = parser.get('PassiveTotal', 'PT_SECRET')

	if PT_KEY == "" or PT_SECRET == "":
		print "  \__", colored("No PassiveTotal API key found :(", 'red')
		return []

	else:
		auth = (PT_KEY, PT_SECRET)
		url = "https://api.passivetotal.org/v2/enrichment/subdomains"
		data = {'query': domain}
		headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0'}

		try:
			response = requests.get(url, auth=auth, json=data, headers=headers)

			if response.status_code == 402:
				print "  \__", colored("Quota exceeded! Bad luck :(", 'red')
				return []

			try:
				for subdomain in response.json()['subdomains']:
					PT.append("%s.%s" % (subdomain, domain))

				PT = set(PT)

				print "  \__", colored("Unique subdomains found:", 'cyan'), colored(len(PT), 'yellow')
				return PT

			except KeyError as errk:
				print "  \__", colored(errk, 'red')
				return []

		except requests.exceptions.RequestException as err:
			print "  \__", colored(err, 'red')
			return []

		except requests.exceptions.HTTPError as errh:
			print "  \__", colored(errh, 'red')
			return []

		except requests.exceptions.ConnectionError as errc:
			print "  \__", colored(errc, 'red')
			return []

		except requests.exceptions.Timeout as errt:
			print "  \__", colored(errt, 'red')
			return []