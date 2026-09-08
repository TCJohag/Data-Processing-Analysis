

class SensorData():
    def __init__(self, device_id, timestamp, value, status):
        self.self = self
        self.device_id = device_id
        self.timestamp = timestamp
        self.value = value
        self.status = status

    def __str__(self):
        return f"{self.device_id, self.timestamp, self.value, self.status}"


class NoDataError(Exception):
    pass


