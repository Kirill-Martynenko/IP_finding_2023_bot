import requests
import abuse

def getVirusTotal(ip_addr, api_key):
	url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
	params = {'apikey':api_key,'ip':ip_addr}
	response = requests.get(url, params=params, timeout=3.5)
	return response.json()

