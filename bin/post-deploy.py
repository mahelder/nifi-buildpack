import os
import requests
import time
from xml.etree import ElementTree

# file_path = '/app/nifi/conf/nifi.properties'

# os.system('sed -i "137s/.*/nifi.web.http.port=5000/ {0}'.format(file_path))

os.system('sh nifi/bin/nifi.sh start')

os.system('sh nifi/bin/nifi.sh run')

# print('ligando nifi')
# time.sleep(30)

# base_url = 'nifi-sample.nifi-sample/nifi'
# base_url_api = 'nifi-sample.nifi-sample/nifi-api'
# response = requests.get(base_url)

# while response.status_code != 200
#     time.sleep(10)
#     response = requests.get(base_url)

# # get process group id
# response = requests.get(base_url_api + '/flow/process-groups/root/status?recursive=true')
# process_group_id = response.json()['processGroupStatus']['id']


# # upload template in process group
# files = {'template': open('template-import.xml')}
# response = requests.post(base_url_api + 'process-groups/{0}/templates/upload'.format(process_group_id), files=files)
# tree = ElementTree.fromstring(response.content)
# template_id = tree[0][2].text


# # activate template in process group
# data = {
#     "originX": 2.0,
#     "originY": 3.0,
#     "templateId": template_id
# }
# response = requests.post(base_url_api + 'process-groups/{0}/template-instance'.format(process_group_id), data=data)


# # start process group
# data = {
#     "id": process_group_id,
#     "state": "RUNNING"
# }
# response = requests.put(base_url_api + 'flow/process-groups/{0}'.format(process_group_id), data=data)

while True:
    time.sleep(30)