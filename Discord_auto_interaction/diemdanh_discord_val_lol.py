import requests
from token_grabber import grab_discord_token

url = "https://discord.com/api/v9/interactions"

token = "lmaoxd"
def diemdanh():
  files=[

  ]
  headers = {
    'authorization': token,
  }

  #diemdanh LOL
  payload = {'payload_json': '{"type":2,"application_id":"1239471466160848957","guild_id":"1040872419784671263","channel_id":"1236227098771853362","session_id":"3497da7fd6f771c924e5ca8f32ef98f8","data":{"version":"1239489153410924622","id":"1239489153217859638","name":"diemdanh","type":1,"options":[],"application_command":{"id":"1239489153217859638","type":1,"application_id":"1239471466160848957","version":"1239489153410924622","name":"diemdanh","description":"Điểm danh hôm nay","dm_permission":true,"integration_types":[0],"permissions":[{"type":3,"id":"1236227098771853362","permission":true},{"type":1,"id":"1040872419784671263","permission":true}],"global_popularity_rank":2,"options":[],"description_localized":"Điểm danh hôm nay","name_localized":"diemdanh"},"attachments":[]},"nonce":null,"analytics_location":"slash_ui"}'}
  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  print(response.text)


  #diemdanh VALORANT
  payload = {'payload_json': '{"type":2,"application_id":"1239471466160848957","guild_id":"1040872419784671263","channel_id":"1236227098771853362","session_id":"3497da7fd6f771c924e5ca8f32ef98f8","data":{"version":"1239489153410924622","id":"1239489153217859638","name":"diemdanh","type":1,"options":[],"application_command":{"id":"1239489153217859638","type":1,"application_id":"1239471466160848957","version":"1239489153410924622","name":"diemdanh","description":"Điểm danh hôm nay","dm_permission":true,"integration_types":[0],"permissions":[{"type":3,"id":"1236227098771853362","permission":true},{"type":1,"id":"1040872419784671263","permission":true}],"global_popularity_rank":2,"options":[],"description_localized":"Điểm danh hôm nay","name_localized":"diemdanh"},"attachments":[]},"nonce":null,"analytics_location":"slash_ui"}'}
  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  print(response.text)
  return response.text

if diemdanh():
  token = grab_discord_token()
  diemdanh()