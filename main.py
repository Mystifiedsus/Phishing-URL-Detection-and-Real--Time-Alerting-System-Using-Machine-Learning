from device import IoTDevice
from attacks import AttackSimulator
from metrics import Metrics
from auth_protocol import AuthProtocol
from utils import print_message_report
import matplotlib.pyplot as plt

# Shared key
KEY = "shared_secret_key"

# Initialize 3 IoT Devices
devices = [IoTDevice(f"ESP8266_{i}", KEY) for i in range(3)]

# Server uses the same key
class Server:
    def __init__(self, key):
        self.protocol = AuthProtocol(key)

server = Server(KEY)

# Send normal messages
normal_messages = [device.send_authenticated_message() for device in devices]
print("\n--- Normal Messages ---")
for msg in normal_messages:
    print_message_report(msg)

# Attack simulations
print("\n--- Replay Attack ---")
replay_messages = [AttackSimulator.replay_attack(normal_messages[0])]
print_message_report(replay_messages[0])

print("\n--- Data Injection Attack ---")
injected_message = AttackSimulator.data_injection(normal_messages[1].copy())
print_message_report(injected_message)

# DoS simulation
print("\n--- DoS Attack (Drop Rate: 50%) ---")
dos_result = AttackSimulator.dos_attack(normal_messages + replay_messages + [injected_message])
print(f"Messages received after DoS: {len(dos_result)}")

# Evaluate metrics
print("\n--- Evaluation Metrics ---")
for msg in normal_messages:
    energy = Metrics.calculate_energy(msg["latency"])
    print(f"{msg['device_id']} - Latency: {round(msg['latency']*1000, 2)} ms | Energy: {energy} mJ")

auth_rate = Metrics.evaluate_authentication(server, normal_messages + replay_messages + [injected_message])
print(f"\nAuthentication Success Rate: {auth_rate:.2f}%")

# Collect metrics for plotting
device_ids = []
latencies = []
energies = []

for msg in normal_messages:
    device_ids.append(msg["device_id"])
    latencies.append(round(msg["latency"] * 1000, 2))  # in ms
    energies.append(Metrics.calculate_energy(msg["latency"]))

# Plot Latency and Energy
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(device_ids, latencies, color='skyblue')
plt.title("Latency per Device")
plt.ylabel("Latency (ms)")
plt.xlabel("Device")

plt.subplot(1, 2, 2)
plt.bar(device_ids, energies, color='salmon')
plt.title("Energy Consumption per Device")
plt.ylabel("Energy (mJ)")
plt.xlabel("Device")

plt.tight_layout()
plt.savefig("latency_energy_plot.png")  # Save as image

# Plot Authentication Success Rate
plt.figure(figsize=(5, 5))
plt.bar(["Success Rate"], [auth_rate], color='lightgreen')
plt.title("Authentication Success Rate")
plt.ylabel("Percentage")
plt.ylim(0, 100)
plt.savefig("auth_success_rate.png")  # Save as image
