import requests

url = "https://discord.com/api/v9/interactions"

payload = {'payload_json': '{"type":2,"application_id":"1239471466160848957","guild_id":"1040872419784671263","channel_id":"1236227098771853362","session_id":"3497da7fd6f771c924e5ca8f32ef98f8","data":{"version":"1239489153410924622","id":"1239489153217859638","name":"diemdanh","type":1,"options":[],"application_command":{"id":"1239489153217859638","type":1,"application_id":"1239471466160848957","version":"1239489153410924622","name":"diemdanh","description":"Điểm danh hôm nay","dm_permission":true,"integration_types":[0],"permissions":[{"type":3,"id":"1236227098771853362","permission":true},{"type":1,"id":"1040872419784671263","permission":true}],"global_popularity_rank":2,"options":[],"description_localized":"Điểm danh hôm nay","name_localized":"diemdanh"},"attachments":[]},"nonce":null,"analytics_location":"slash_ui"}'}
files=[

]
headers = {
  'authorization': 'Nzc4MjY4MTgyNzE2MjE5NDIz.GZ0AFI.VKXekUihy37VIXfBQiSSUeKg_KROnGWa0LBbNo',
  #'Cookie': '__cfruid=d86213e0afba19e1aa769faca90b3d7a3a731691-1727893820; __dcfduid=641a88d680ec11ef935712576fa9bc6a; __sdcfduid=641a88d680ec11ef935712576fa9bc6ae6a206cd5245c5e7fe3b81c2ad1b7d0ebb56ea544c4914691a152b154ed0d2fc; _cfuvid=djmvm7cGfjjRCmx74f.ToCKp5RJPS8BoUYJNeSRfWy0-1727893820905-0.0.1.1-604800000'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
