import requests

Auth = "Nzc4MjY4MTgyNzE2MjE5NDIz.GuG7W8.HVPVsPpol88NPxvcYbVILjgwxmF4BiHQhlGMoE"
def diemDanhVal():

    url = "https://discord.com/api/v9/interactions"

    payload = {'payload_json': '{"type":2,"application_id":"1117099742921502850","guild_id":"653508294962315285","channel_id":"1135209424538062858","session_id":"d7e1beece190ce35393f2cebee466b5c","data":{"version":"1123118111294500886","id":"1123118111189639172","name":"diemdanh","type":1,"options":[],"application_command":{"id":"1123118111189639172","type":1,"application_id":"1117099742921502850","version":"1123118111294500886","name":"diemdanh","description":"Điểm danh hôm nay","integration_types":[0],"permissions":[{"type":3,"id":"1135209424538062858","permission":true},{"type":1,"id":"653508294962315285","permission":true}],"options":[],"description_localized":"Điểm danh hôm nay","name_localized":"diemdanh"},"attachments":[]},"nonce":null,"analytics_location":"slash_ui"}'}
    files=[

    ]
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Authorization': Auth,
    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEyMS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyMS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIxLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjU2MjMxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9',
    'X-Discord-Locale': 'vi',
    'X-Discord-Timezone': 'Asia/Bangkok',
    'X-Debug-Options': 'bugReporterEnabled',
    'Origin': 'https://discord.com',
    'Alt-Used': 'discord.com',
    'Connection': 'keep-alive',
    'Referer': 'https://discord.com/channels/653508294962315285/1135209424538062858',
    'Cookie': '__dcfduid=3cf63060ade411ee9160c186bb850f98; __sdcfduid=3cf63061ade411ee9160c186bb850f989ffd8a94667abd513f6a243d7680ec7d89668f7108426c9396ba05fc53f0150a; __cfruid=dbdaf2d3ae3db6067bf46a9250017c50d4a77db1-1704690628; _cfuvid=7ayDFVMbW8skGNcu0Gr_GXVhSgfoJIhQaed_hE0y6SI-1704690628209-0-604800000; cf_clearance=DZG2HtFR.RFUbZwFMtsfnSyEBqzXkT2G1MU8lXjxFcA-1704690629-0-2-27b67f33.a4f91862.8c785d43-0.2.1704690629; locale=vi; OptanonConsent=isIABGlobal=false&datestamp=Mon+Jan+08+2024+12%3A09%3A58+GMT%2B0700+(Indochina+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


def diemDanhLol():

    url = "https://discord.com/api/v9/interactions"

    payload = {'payload_json': '{"type":2,"application_id":"1239471466160848957","guild_id":"1040872419784671263","channel_id":"1236227098771853362","session_id":"43814d02ba448038a76682eecd0d1c87","data":{"version":"1239489153410924622","id":"1239489153217859638","name":"diemdanh","type":1,"options":[],"application_command":{"id":"1239489153217859638","type":1,"application_id":"1239471466160848957","version":"1239489153410924622","name":"diemdanh","description":"Điểm danh hôm nay","dm_permission":true,"integration_types":[0],"permissions":[{"type":3,"id":"1236227098771853362","permission":true}],"global_popularity_rank":3,"options":[],"description_localized":"Điểm danh hôm nay","name_localized":"diemdanh"},"attachments":[]},"nonce":null,"analytics_location":"slash_ui"}'}
    files=[

    ]
    headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'authorization': Auth,
    'cookie': '__dcfduid=d81cfd60ba0711ee84e16fd0a06a1300; __sdcfduid=d81cfd61ba0711ee84e16fd0a06a1300b90005b2e8896a98e199e817f11415ffdca721dbdd0e1599d08574a8e1d473cc; __cfruid=64c7551b1b5701d22c26790ffbba49ae29f87d2a-1717936963; _cfuvid=2qMt0w7ttc2lGEm.MPV_Tbb19Qw8OLtg9AYEdnnNm3Y-1717936963866-0.0.1.1-604800000; cf_clearance=yhfgyH0rd8zBiR.dPJzRkmjNXil6q6hkcRmWhIIQi.U-1717936966-1.0.1.1-.IzTLuNF502VQhD2j_rddnAybGA6MEsMZb1cmgR_nBMAj4Fx66M8oeAz1sJOkaLN5E0pLxMiSqkwooCaJpFYpQ; OptanonConsent=isIABGlobal=false&datestamp=Sun+Jun+09+2024+19%3A42%3A52+GMT%2B0700+(Indochina+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; locale=vi; __cfruid=dd19d46a4dad85129c516a4f6db7725a5ab49bea-1717937538; __dcfduid=1addc94a265f11ef9cf94a2bcf0e7262; __sdcfduid=1addc94a265f11ef9cf94a2bcf0e72620dca06a3be1ea2e358e72d8cdaa12b8f0ba56a4a79e31a4150c1f4f7c07ef653; _cfuvid=SfVXf0g3TdrSlqgbHNQoPv.9vLl8TiEKpjkTRcLSdaI-1717937538735-0.0.1.1-604800000',
    'origin': 'https://discord.com',
    'priority': 'u=1, i',
    'referer': 'https://discord.com/channels/1040872419784671263/1236227098771853362',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'vi',
    'x-discord-timezone': 'Asia/Saigon',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InZpLVZOIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwMDEwOSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)



def diemDanh():
    diemDanhLol()
    diemDanhVal()

diemDanh()
input("Tasks ran successfully. Press ENTER to continue.")