
"""
Utility Functions
"""
from datetime import datetime

def normalize_mac(mac: str) -> str:
    """
    Normalize MAC address into lowercase colon-separated format.
    """
    return mac.lower().replace("-", ":").replace(".", ":")


def current_timestamp() -> str:
    """
    Return the current timestamp in YYYY-MM-DD HH:MM:SS format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")