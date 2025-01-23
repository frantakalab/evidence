import requests
import json

# STEP 1: Set your Strava App details
CLIENT_ID = 'XXXX'
CLIENT_SECRET = 'XXXX'
REDIRECT_URI = 'http://localhost'  # Or your actual redirect URI

# STEP 2: Authenticate and get the authorization code
print("Visit the following URL to authorize your app:")
auth_url = f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=read,activity:read_all"
print(auth_url)

authorization_code = input("Enter the authorization code you received: ")

# STEP 3: Exchange the authorization code for an access token
token_url = "https://www.strava.com/oauth/token"
token_data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "code": authorization_code,
    "grant_type": "authorization_code"
}

response = requests.post(token_url, data=token_data)
if response.status_code == 200:
    tokens = response.json()
    access_token = tokens['access_token']
    refresh_token = tokens['refresh_token']
    expires_at = tokens['expires_at']
    print("Access Token:", access_token)
else:
    print("Failed to get access token:", response.json())
    exit()

# Step 3: Fetch All Activities Using Pagination
activities_url = "https://www.strava.com/api/v3/athlete/activities"
headers = {"Authorization": f"Bearer {access_token}"}

all_activities = []
page = 1
per_page = 50  # Maximum allowed is 200, but 50 is a good starting point for testing.

while True:
    print(f"Fetching page {page}...")
    params = {"page": page, "per_page": per_page}
    response = requests.get(activities_url, headers=headers, params=params)
    if response.status_code == 200:
        activities = response.json()
        if not activities:  # Exit the loop if no more activities are returned
            break
        all_activities.extend(activities)
        page += 1
    else:
        print("Error fetching activities:", response.json())
        break

print(f"Total activities fetched: {len(all_activities)}")

# Save all activities to a JSON file
with open('all_strava_activities.json', 'w') as f:
    json.dump(all_activities, f, indent=4)
    print("All activities saved to 'all_strava_activities.json'.")
