import requests
import time
import json
# Function to sign in and get token
def get_token_and_accountId(email, password):
    url = "https://api.hsa.edu.vn/accounts/sign-in"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "content-type": "application/json"
    }
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["token"], response.json()["accountInfo"]["id"]
    else:
        print("Failed to sign in.")
        return None

# Function to get available exam locations
def get_exam_locations(periodId, token):
    querystring = {"periodId":periodId,"batchId":batchId}
    url = f"https://api.hsa.edu.vn/exam/views/registration/available-location"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get exam locations.")
        return None


# Function to check available slots at a location
def check_available_slots(periodId, locationId, token):
    querystring = {"periodId":periodId,"locationId": locationId,"batchId":batchId}
    url = f"https://api.hsa.edu.vn/exam/views/registration/available-slot"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to check available slots.")
        return None
    
def register(accountId, periodId, batchId, locationId, slotId, token):
    url = f"https://api.hsa.edu.vn/exam/register?accountId={accountId}"

    payload = json.dumps({
    "record": {
        "periodId": periodId,
        "batchId": batchId,
        "locationId": locationId,
        "slotId": slotId
    }
    })

    headers = {
    'Accept': 'application/json, text/plain, */*',
    "Authorization": f"Bearer {token}",
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://id.hsa.edu.vn',
    'Referer': 'https://id.hsa.edu.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    #notify phone
    requests.post("https://ntfy.sh/ScopenTest",
    data=response.text.encode(encoding='utf-8'))


# Credentials
email = "burner account@gmail.com"
password = "hmmmmmmmmmmmm"

# Period ID for which you want to check the exam locations
periodId = 35 #const 
batchId_list = [76]#batch == dot thi / 73 == 404, 74 == 405, 75 == 406 [72, 73, 74, 75]
batch_list = [407] # [403, 404, 405, 406]



loopCondition = True
while loopCondition:

    #Get token
    tuple = get_token_and_accountId(email, password)
    token, accountId = tuple
    if token and accountId:
        pass
    else:
        print("Failed to get token. Check credentials.")

    for batchId in batchId_list:
        batch = batch_list[batchId_list.index(batchId)]
        # Get available exam locations
        exam_locations = get_exam_locations(periodId, token)
        if exam_locations:
            for location in exam_locations:                
                # Check available slots for each location
                locationId = location["id"]
                slots = check_available_slots(periodId, locationId, token)
                if slots:
                    for slot in slots:
                        if {slot['registeredSlots']} == {slot['numberOfSeats']}:
                            #print(f"{batch}: {location['name']} - {slot['name']} - {slot['registeredSlots']} out of {slot['numberOfSeats']}") 
                            pass

                        else:
                            slotId = slot["id"]
                            available_slot = slot['numberOfSeats'] - slot['registeredSlots']
                            if available_slot > 0:
                                message = f"{batch}: {location['name']} - {slot['name']} - còn lại {available_slot}"


                                print(message)
                                #if batch == 404:
                                if (batch == 401 and ("Thanh H" in message or "Hà Nội" in message or "Ninh Bình" in message or "Vinh" in message)):
                                    
                                    email = "real_account@gmail.com"
                                    password = "password"

                                    #Get token
                                    tuple = get_token_and_accountId(email, password)
                                    token, accountId = tuple
                                    if token and accountId:
                                        pass
                                    else:
                                        print("Failed to get token. Check credentials.")

                                    register(accountId, periodId, batchId, locationId, slotId, token)
                                    loopCondition = False
                                time.sleep(10)
                else:
                    pass
                    print(f"Failed to fetch available slots for {batch}: {location['name']} {slot['name']}.")
