import os
from groq import Groq

question = "How are you?"

os.environ["GROQ_API_KEY"] = "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"

# Create the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"), )

chat_completion = client.chat.completions.create(
    messages=[
        {
                "role": "system",
                "content":
                "You are a helpful assistant. You reply with very short answers.",
        }
    ],
    model="llama3-8b-8192",
)

chat_response = chat_completion.choices[0].message.content
final_ans = chat_response
print(chat_response)
