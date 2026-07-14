"""
Device Manager

Maintains all discovered devices.
"""

from src.device import Device


class DeviceManager:

    def __init__(self):

        self.devices = {}

    def add_device(self, mac):

        if mac not in self.devices:

            self.devices[mac] = Device(mac)

        return self.devices[mac]

    def get_device(self, mac):

        return self.devices.get(mac)

    def all_devices(self):

        return list(self.devices.values())

    def total_devices(self):

        return len(self.devices)