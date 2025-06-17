import requests

def get_top_abuse_ips():
    url = "https://api.abuseipdb.com/api/v2/blacklist"
    headers = {
        "Key": "b48c5b8b4a953eab09f319812f6b3174a9edcfcfd31ee9006c9d3ca7757613d9f17e9cb69fa0f420",
        "Accept": "application/json"
    }
    params = {
        "confidenceMinimum": "90",
        "limit": "10"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return [ip['ipAddress'] for ip in data.get("data", [])]
    except Exception as e:
        return [f"Error fetching data: {e}"]
