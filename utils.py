def print_message_report(msg):
    print(f"Device: {msg['device_id']} | Data: {msg['data']} | Nonce: {msg['nonce']} | Token: {msg['token'][:8]}... | Latency: {round(msg['latency']*1000, 2)} ms")
