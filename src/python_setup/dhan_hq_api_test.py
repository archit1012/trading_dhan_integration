import os
from dotenv import load_dotenv
from dhanhq import dhanhq

load_dotenv()

client_id = os.getenv("DHAN_CLIENT_ID")
access_token = os.getenv("DHAN_ACCESS_TOKEN")

# Initialize the official Dhan client
dhan = dhanhq(client_id, access_token)

# Test the API connection by pulling fund limits
try:
    funds_data = dhan.get_fund_limits()
    if funds_data.get("status") == "success":
        print("Success! Official Dhan API connection established.")
        print("Fund Details:", funds_data)
    else:
        print("Failed to authenticate. Response:", funds_data)
except Exception as e:
    print(f"An error occurred: {e}")
