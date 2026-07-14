"""
Device model used by the Network Monitoring System.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Set


@dataclass
class Device:
    """
    Represents a single network device.
    """

    mac: str

    ips: Set[str] = field(default_factory=set)

    vendor: str = "Unknown"

    status: str = "Pending"

    confidence: int = 0

    open_ports: Set[int] = field(default_factory=set)

    seen_by: Set[str] = field(default_factory=set)

    first_seen: datetime = field(default_factory=datetime.now)

    last_seen: datetime = field(default_factory=datetime.now)

    missed_scans: int = 0

    def update(
        self,
        ip=None,
        vendor=None,
        method=None,
        ports=None
    ):
        """
        Update device information after discovery.
        """

        self.last_seen = datetime.now()

        self.status = "Online"

        self.missed_scans = 0

        if ip:
            self.ips.add(ip)

        if vendor:
            self.vendor = vendor

        if method:
            self.seen_by.add(method)

        if ports:
            self.open_ports.update(ports)

        self.confidence = min(self.confidence + 10, 100)

    def mark_pending(self):
        """
        Mark device as pending.
        """

        self.status = "Pending"

    def mark_offline(self):
        """
        Mark device as offline.
        """

        self.status = "Offline"

    def mark_online(self):
        """
        Mark device as online.
        """

        self.status = "Online"

        self.last_seen = datetime.now()

    def increase_miss(self):
        """
        Increase missed scan count.
        """

        self.missed_scans += 1

    def to_dict(self):
        """
        Convert device object into dictionary.
        """

        return {

            "mac": self.mac,

            "ips": ", ".join(sorted(self.ips)),

            "vendor": self.vendor,

            "status": self.status,

            "confidence": self.confidence,

            "ports": ", ".join(
                str(port)
                for port in sorted(self.open_ports)
            ),

            "seen_by": ", ".join(sorted(self.seen_by)),

            "first_seen": self.first_seen.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "last_seen": self.last_seen.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }