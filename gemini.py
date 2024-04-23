import os
import requests
import json

def gemini(prompt):

    apikey = 'Enter the API KEY of Gemini'
    headers = {
        'Content-Type': 'application/json',
    }

    params = {
        'key': apikey,
    }

    json_data = {
        'contents': [
            {
                'parts': [
                    {
                        'text': prompt,
                    },
                ],
            },
        ],
    }

    response = requests.post(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent',
        params=params,
        headers=headers,
        json=json_data,
    )
    return json.loads(response.content)["candidates"][0]["content"]["parts"][0]["text"]

