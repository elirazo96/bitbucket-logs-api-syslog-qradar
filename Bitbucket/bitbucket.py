# elirazo96
import requests
import json
from datetime import datetime, timedelta

def fetch_bitbucket_logs(org_id, access_token):
    url = f"https://api.atlassian.com/admin/v1/orgs/{org_id}/events"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        current_time = datetime.utcnow()

        # Filter and write logs
        logs = [item for item in data["data"] if is_recent_log(item, current_time)]
        write_logs(logs)

    except requests.RequestException as e:
        print(f"Error fetching Bitbucket logs: {e}")

def is_recent_log(log_item, current_time):
    event_time = datetime.strptime(log_item["attributes"]["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    time_difference = current_time - event_time
    return time_difference.total_seconds() <= 300

def write_logs(logs):
    for count, log_item in enumerate(logs):
        file_path = f"/root/Bitbucket/logs/alert_{count}.json"
        with open(file_path, "w") as fileObj:
            json.dump(log_item, fileObj)

# Example usage
org_id = "<your_org_id>"
access_token = "<your_access_token>"
fetch_bitbucket_logs(org_id, access_token)



