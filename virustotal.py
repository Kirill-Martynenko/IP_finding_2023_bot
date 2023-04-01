from vtapi3 import VirusTotalAPIIPAddresses, VirusTotalAPIError
import json

class result_string:
    text = ""

    def add_text(self, s):
        self.text += s

def getVirusTotal(ip_addr, api_key):
    result = result_string()
    vt_api_ip_addresses = VirusTotalAPIIPAddresses(api_key)
    try:
        output = vt_api_ip_addresses.get_report(ip_addr)
    except VirusTotalAPIError as err:
        return(err + err.err_code)
    else:
        if vt_api_ip_addresses.get_last_http_error() == vt_api_ip_addresses.HTTP_OK:
            output = json.loads(output)
            try:
                result.add_text("Network: " + output["data"]["attributes"]["network"] + "\n")
            except KeyError:
                result.add_text("Network: unknown\n")
            try:
                result.add_text("Country: " + output["data"]["attributes"]["country"] + "\n")
            except KeyError:
                result.add_text("Country: unknown \n")
            try:
                result.add_text("Owner: " + output["data"]["attributes"]["as_owner"] + "\n")
            except KeyError:
                result.add_text("Owner: unknown\n")
            result.add_text("Last analysis stats:")
            result.add_text("\n" + "\t\t\t\t")
            result.add_text("harmless: " + str(output["data"]["attributes"]["last_analysis_stats"]["harmless"]))
            result.add_text("\n" + "\t\t\t\t")
            result.add_text("malicious: " + str(output["data"]["attributes"]["last_analysis_stats"]["malicious"]))
            result.add_text("\n" + "\t\t\t\t")
            result.add_text("suspicious: " + str(output["data"]["attributes"]["last_analysis_stats"]["suspicious"]))
            result.add_text("\n" + "\t\t\t\t")
            result.add_text("undetected: " + str(output["data"]["attributes"]["last_analysis_stats"]["undetected"]))
            result.add_text("\n" + "\t\t\t\t")
            result.add_text("timeout: " + str(output["data"]["attributes"]["last_analysis_stats"]["timeout"]) + "\n")
            try:
                result.add_text("asn: " + str(output["data"]["attributes"]["asn"]) + "\n")
            except KeyError:
                result.add_text("asn: unknown\n")
            result.add_text("id: " + output["data"]["id"])
            return(result.text)
        else:
            return('HTTP Error [' + str(vt_api_ip_addresses.get_last_http_error()) + ']')