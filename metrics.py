class Metrics:
    @staticmethod
    def calculate_energy(latency):
        # Assume 50mW power usage and convert to mJ (Energy = Power × Time)
        return round(0.05 * latency * 1000, 4)

    @staticmethod
    def evaluate_authentication(server, messages):
        success = 0
        for msg in messages:
            result = server.protocol.verify_auth_token(msg["data"], msg["nonce"], msg["token"])
            if result:
                success += 1
        return success / len(messages) * 100
