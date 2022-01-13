#Toolbox batch API run showing iterating over files, running a tool on them and getting results back
#sample for https://toolbox.nextgis.com/operation/kml2geodata

import requests
import glob,sys,time
import urllib3
urllib3.disable_warnings()

##############################################
token = 'YOUR API TOKEN'
input_folder = 'c:\\Work\\test\\'
operation = 'kml2geodata'
##############################################

headers = {'Authorization': 'Token %s' % token}

input_files = glob.glob(input_folder + '*.kmz')

for f in input_files:
    # Upload files
    url = 'https://toolbox.nextgis.com/api/upload/'
    files = {}
    file = open(f, 'rb')
    response = requests.post(url, data=file, headers=headers, verify=False)
    files['kmlfile'] = response.text

    # Create request
    json_request = {'operation': operation, 'inputs': {}}
    json_request['inputs']['ngdriveid'] = ''
    json_request['inputs']['fields'] = 'test'
    json_request['inputs']['kmlfile'] = files['kmlfile']

    # Run tool
    url = 'https://toolbox.nextgis.com/api/json/execute/'
    response = requests.post(url, json=json_request, headers=headers, verify=False)
    task_id = response.json()['task_id']
    
    print('\nWorking on...' + f)

    # Wait for completion
    task_state = "UNKNOWN"
    url = 'https://toolbox.nextgis.com/api/json/status/{task_id}/'.format(task_id=task_id)
    while task_state in ["UNKNOWN", "ACCEPTED", "STARTED"]:
        time.sleep(1)
        sys.stdout.write('.')
        sys.stdout.flush()

        # Check state
        response = requests.get(url, headers=headers, verify=False)
        task_state = response.json().get("state")
    
    # Download results
    if task_state == "SUCCESS":
        response = requests.get(response.json()['output'][0]["value"], verify=False)
        f_output = f.replace('.kmz','_output.zip')
        with open(f_output, 'wb') as f:
            for chunk in response.iter_content(chunk_size=512 * 1024):
                if chunk:
                    f.write(chunk)