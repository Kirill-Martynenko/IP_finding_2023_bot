import requests

def abuse(ip):
	url = 'https://api.abuseipdb.com/api/v2/check'
	querystring = {
	    'ipAddress': ip,
	    'maxAgeInDays': '90'
	}
	headers = {
	    'Accept': 'application/json',
    'Key': 'aed61328696d120ffb33fed3513f4a729edf3d67c9d6dc25c36f2e2107369889b182c28882e73865'
	}
	response = requests.request(method='GET', url=url, headers=headers, params=querystring)
	print(response.text)


abuse('46.56.101.2')