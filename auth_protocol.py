import hmac
import hashlib
import os

class AuthProtocol:
    def __init__(self, key):
        self.key = key

    def generate_nonce(self):
        return os.urandom(8).hex()

    def generate_auth_token(self, message, nonce):
        data = f"{message}:{nonce}"
        return hmac.new(self.key.encode(), data.encode(), hashlib.sha256).hexdigest()

    def verify_auth_token(self, message, nonce, token):
        expected = self.generate_auth_token(message, nonce)
        return hmac.compare_digest(expected, token)
