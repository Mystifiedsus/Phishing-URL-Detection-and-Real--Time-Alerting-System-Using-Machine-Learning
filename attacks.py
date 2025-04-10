import random

class AttackSimulator:
    @staticmethod
    def data_injection(message):
        fake_data = "99.99:99.99"
        message["data"] = fake_data
        return message

    @staticmethod
    def replay_attack(original_message):
        return original_message  # Reuse same message

    @staticmethod
    def dos_attack(messages, drop_rate=0.5):
        return [msg for msg in messages if random.random() > drop_rate]
