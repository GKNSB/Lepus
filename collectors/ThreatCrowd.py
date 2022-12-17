import requests
from http.client import responses
from json import loads
from termcolor import colored
from urllib3.exceptions import InsecureRequestWarning


def init(domain):
	TC = []

	print(colored("[*]-Searching ThreatCrowd...", "yellow"))
	requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

	try:
		result = requests.get("https://www.threatcrowd.org/searchApi/v2/domain/report/", params={"domain": domain}, verify=False)

		if result.status_code == 200:
			try:
				RES = loads(result.text)
				resp_code = int(RES["response_code"])

				if resp_code == 1:
					for sd in RES["subdomains"]:
						TC.append(sd)

				TC = set(TC)

				print("  \__ {0}: {1}".format(colored("Subdomains found", "cyan"), colored(len(TC), "yellow")))
				return TC

			except ValueError as errv:
				print("  \__", colored(errv, "red"))
				return []

		else:
			print("  \__", colored("Response: {0} {1}".format(result.status_code, responses[result.status_code]), "red"))
			return []

	except requests.exceptions.RequestException as err:
		print("  \__", colored(err, "red"))
		return []

	except requests.exceptions.HTTPError as errh:
		print("  \__", colored(errh, "red"))
		return []

	except requests.exceptions.ConnectionError as errc:
		print("  \__", colored(errc, "red"))
		return []

	except requests.exceptions.Timeout as errt:
		print("  \__", colored(errt, "red"))
		return []

	except Exception:
		print("  \__", colored("Something went wrong!", "red"))
		return []
