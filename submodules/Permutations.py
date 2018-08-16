from termcolor import colored


def permuteDash(subdomain, wordlist):
	results = []

	for word in wordlist:
		results.append('-'.join([word, subdomain]))
		results.append('-'.join([subdomain, word]))

	if "." in subdomain:
		subParts = subdomain.split(".")

		for part in subParts:
			for word in wordlist:
				results.append(subdomain.replace(part, '-'.join([word, part])))
				results.append(subdomain.replace(part, '-'.join([part, word])))

	return results


def permuteDot(subdomain, wordlist):
	results = []

	for word in wordlist:
		results.append('.'.join([word, subdomain]))
		results.append('.'.join([subdomain, word]))

	if "." in subdomain:
		subParts = subdomain.split(".")

		for part in subParts:
			for word in wordlist:
				results.append(subdomain.replace(part, '.'.join([word, part])))

	return results


def permuteWords(subdomain, wordlist):
	results = []

	for word in wordlist:
		results.append(''.join([word, subdomain]))
		results.append(''.join([subdomain, word]))

	if "." in subdomain:
		subParts = subdomain.split(".")

		for part in subParts:
			for word in wordlist:
				results.append(subdomain.replace(part, ''.join([word, part])))
				results.append(subdomain.replace(part, ''.join([part, word])))

	return results


def permuteNumbers(subdomain):
	results = []

	for number in range(10):
		results.append('-'.join([subdomain, str(number)]))
		results.append(''.join([subdomain, str(number)]))

	if "." in subdomain:
		subParts = subdomain.split(".")

		for part in subParts:
			for number in range(10):
				results.append(subdomain.replace(part, '-'.join([part, str(number)])))
				results.append(subdomain.replace(part, ''.join([part, str(number)])))

	return results


def init(domain, subdomains, wordlist):
	print "{0} {1} {2}".format(colored("\n[*]-Performing permutations on", "yellow"), colored(len(subdomains), "cyan"), colored("resolved hostnames...", "yellow"))

	permutated_subdomains = []
	permutations = []
	words = []

	try:
		with open(wordlist, "r") as wordListFile:
			for line in wordListFile:
				words.append(line.strip())

	except OSError:
		return None

	except IOError:
		return None

	for subdomain in subdomains:
		subdomain = subdomain.split(domain)[0][:-1]
		permutated_subdomains += permuteDash(subdomain, words)
		permutated_subdomains += permuteDot(subdomain, words)
		permutated_subdomains += permuteWords(subdomain, words)
		permutated_subdomains += permuteNumbers(subdomain)

	permutated_subdomains = set(permutated_subdomains)

	for subdomain in permutated_subdomains:
		permutations.append('.'.join([subdomain, domain]))

	print "  \__", colored("Generated subdomains:", 'cyan'), colored(len(permutations), 'yellow')
	return permutations