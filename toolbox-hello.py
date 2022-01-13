#Simplest Toolbox API run
#working version for https://toolbox.nextgis.com/operation/hello

import requests

##############SET THESE#######################
token = 'YOUR API TOKEN'
operation = 'hello'
##############################################

headers = {'Authorization': 'Token %s' % token}
json_request = {'operation': operation, 'inputs': {}}
json_request['inputs']['name'] = 'sdfsd' #5 symbols max here
url = 'https://toolbox.nextgis.com/api/json/execute/'
response = requests.post(url, json=json_request, headers=headers, verify=False)
print(response.text)