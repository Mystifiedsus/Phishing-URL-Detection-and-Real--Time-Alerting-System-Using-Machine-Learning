import time
import random
from auth_protocol import AuthProtocol

class IoTDevice:
    def __init__(self, device_id, key):
        self.device_id = device_id
        self.protocol = AuthProtocol(key)

    def read_sensor_data(self):
        temp = round(random.uniform(20, 35), 2)
        humidity = round(random.uniform(30, 70), 2)
        return f"{temp}:{humidity}"

    def send_authenticated_message(self):
        start_time = time.time()
        data = self.read_sensor_data()
        nonce = self.protocol.generate_nonce()
        token = self.protocol.generate_auth_token(data, nonce)
        end_time = time.time()
        latency = end_time - start_time
        return {
            "device_id": self.device_id,
            "data": data,
            "nonce": nonce,
            "token": token,
            "latency": latency
        }
