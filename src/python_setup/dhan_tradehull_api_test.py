import os
from dotenv import load_dotenv
from Dhan_Tradehull import Tradehull

# Replace with your actual credentials
load_dotenv()

client_id = os.getenv("DHAN_CLIENT_ID")
access_token = os.getenv("DHAN_ACCESS_TOKEN")

# Initialize the Tradehull client wrapper
tsl = Tradehull(client_id, access_token)

# Test the API by requesting the Last Traded Price (LTP) for a stable ticker
try:
    # Fetches standard market data structure via Tradehull framework
    ltp_data = tsl.get_intraday_data('SBIN', 'NSE', 1)
    print("Success! Dhan-Tradehull library is configured properly.")
    print("Sample Data Output:", ltp_data.head(2) if hasattr(ltp_data, 'head') else ltp_data)
except Exception as e:
    print(f"Failed to authenticate or fetch data via Tradehull: {e}")
