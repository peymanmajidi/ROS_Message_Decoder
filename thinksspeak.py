import requests

URL = "https://api.thingspeak.com/update?api_key=CE2FWBEV0SX314V6&field1=1&"
def api(data):
    parameters = ''
    for item in data:
        parameters = parameters + "&" if parameters != '' else parameters
        parameters += f"{item['key']}={item['value']}"

    
    url = URL + "?" + parameters
    print(url)