import requests

def getVirusTotal(ip_addr, api_key):
	url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
	params = {'apikey':api_key,'ip':ip_addr}
	response = requests.get(url, params=params)
	return response.json()

