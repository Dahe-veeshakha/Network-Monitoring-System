"""
Utility functions used across the Network Monitoring System.

This module provides helper functions for:

- MAC address normalization
- Timestamp generation
"""

from datetime import datetime


def normalize_mac(mac: str) -> str:
    """
    Normalize a MAC address into lowercase colon-separated format.

    Example:
        AA-BB-CC-DD-EE-FF
        aa.bb.cc.dd.ee.ff

    becomes

        aa:bb:cc:dd:ee:ff
    """

    if not mac:
        return ""

    return (
        mac.lower()
        .replace("-", ":")
        .replace(".", ":")
        .strip()
    )


def current_timestamp() -> str:
    """
    Return current local timestamp.

    Format:
        YYYY-MM-DD HH:MM:SS
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")