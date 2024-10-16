import requests
import json

# Ask the user for the input code
input_code = input("Please enter the Quizizz code: ")

# API request
url = "https://v3.schoolcheats.net/quizizz/answers"
payload = json.dumps({
  "input": input_code
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# Parse the JSON response
data = json.loads(response.text)

# Check if the response contains the expected structure
if 'questions' in data:
    # Iterate through each question in the 'questions' list
    for index, question in enumerate(data['questions'], start=1):
        # Extract the question text
        question_text = question['structure']['query']['text']
        
        # Extract the correct answer
        correct_answer_index = question['structure']['answer']
        correct_answer_text = question['structure']['options'][correct_answer_index]['text']
        
        # Print the question and answer
        print(f"Question {index}: {question_text}")
        print(f"Answer: {correct_answer_text}")
        print()  # Add a blank line for readability
else:
    print("The API response doesn't contain the expected 'questions' key.")
    print("API Response:", response.text)