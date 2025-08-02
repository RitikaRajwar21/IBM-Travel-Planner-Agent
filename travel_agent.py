import requests
API_KEY = "ApiKey-61ee5ac3-25ae-4930-be20-161e5b50919b"
URL = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/28031ebb-a9ab-4699-bab8-80f07206da32/ai_service?version=2021-05-01"

# Step 2: Headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Step 3: Input Data (User Query)
data = {
    "input": "Plan a 3-day trip to Manali under 10000 INR"
}

# Step 4: Send POST Request
response = requests.post(URL, headers=headers, json=data)

# Step 5: Show Output
print(response.json())
