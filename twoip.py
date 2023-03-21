import requests
def twoip(ip):
	url = 'http://ip-api.com/json/ip'
	params = {'ip':ip}
	querystring = {
	    'ipAddress': ip,
	    'maxAgeInDays': '90'
	}
	headers = {
	    'Accept': 'http://ip-api.com/json',
	}
	response = requests.request(method='GET', url=url, headers=headers, params=querystring)
	return response.text
