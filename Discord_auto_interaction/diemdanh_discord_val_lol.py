import requests
from token_grabber import grab_discord_token
from datetime import datetime
url = "https://discord.com/api/v9/interactions"

def diemdanh():
    files = []

    # Read the token from a file
    with open('token.txt', 'r') as file:
        token = file.read().strip()

    headers = {
        'authorization': token,
    }

    # diemdanh LOL
    payload = {'payload_json': '{"type":2,"application_id":"1239471466160848957","guild_id":"1040872419784671263","channel_id":"1236227098771853362","session_id":"3497da7fd6f771c924e5ca8f32ef98f8","data":{"version":"1239489153410924622","id":"1239489153217859638","name":"diemdanh","type":1,"options":[],"application_command":{"id":"1239489153217859638","type":1,"application_id":"1239471466160848957","version":"1239489153410924622","name":"diemdanh","description":"Điểm danh hôm nay","dm_permission":true,"integration_types":[0],"permissions":[{"type":3,"id":"1236227098771853362","permission":true},{"type":1,"id":"1040872419784671263","permission":true}],"global_popularity_rank":2,"options":[],"description_localized":"Điểm danh hôm nay","name_localized":"diemdanh"},"attachments":[]},"nonce":null,"analytics_location":"slash_ui"}'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    message = f"Đã điểm danh LOL. Status code: {response.status_code}. Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    print(message)
    requests.post("https://ntfy.sh/scopentest", data=message.encode(encoding='utf-8'))

    if response.status_code == 401:
        return True

    # diemdanh VALORANT
    payload = {'payload_json': '{"type":2,"application_id":"1117099742921502850","guild_id":"653508294962315285","channel_id":"1135209424538062858","session_id":"d3394e4ba359d3e961cde65d327767d1","data":{"version":"1123118111294500886","id":"1123118111189639172","name":"diemdanh","type":1,"options":[],"application_command":{"id":"1123118111189639172","type":1,"application_id":"1117099742921502850","version":"1123118111294500886","name":"diemdanh","description":"Điểm danh hôm nay","dm_permission":true,"integration_types":[0],"permissions":[{"type":3,"id":"1135209424538062858","permission":true},{"type":1,"id":"653508294962315285","permission":true}],"global_popularity_rank":3,"options":[],"description_localized":"Điểm danh hôm nay","name_localized":"diemdanh"},"attachments":[]},"nonce":null,"analytics_location":"slash_ui"}'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    message = f"Đã điểm danh VALORANT. Status code: {response.status_code}. Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    print(message)
    requests.post("https://ntfy.sh/scopentest", data=message.encode(encoding='utf-8'))

    return (response.status_code == 401)

# Run the function and check if the token is invalid
if diemdanh():
    error = ("Token is invalid. Please scan the QR code to get a new token.")
    print(error)
    requests.post("https://ntfy.sh/scopentest", data=error.encode(encoding='utf-8'))

    token = grab_discord_token()
    
    # Write the token to a file
    with open('token.txt', 'w') as file:
        file.write(token)
    
    diemdanh()