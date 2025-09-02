# IoT Device Security Simulation

This project is a Python-based simulation demonstrating a simple authentication protocol for IoT devices and its vulnerability to common cyberattacks. It provides a foundational understanding of how replay, data injection, and denial-of-service (DoS) attacks can affect a network of IoT devices and how an authentication protocol can mitigate some of these threats.

---

## 🚀 Features

- **Simulated IoT Devices**: Creates and manages multiple IoT devices that can send authenticated messages.  
- **Authentication Protocol**: Implements a simple shared-key authentication scheme to verify message integrity and origin.  
- **Attack Simulation**: Includes classes to simulate three major types of attacks:  
  - 🔁 **Replay Attack**: Re-sends a previously valid message to the server.  
  - 📝 **Data Injection Attack**: Modifies the content of a valid message to inject malicious data.  
  - ⛔ **Denial-of-Service (DoS) Attack**: Simulates network congestion by dropping a percentage of messages.  
- **Performance Metrics**: Evaluates and reports key performance metrics such as latency, energy consumption, and authentication success rate.  
- **Data Visualization**: Generates and saves plots to visualize key metrics, providing a clear summary of the simulation results.  

---

## ⚙️ How to Run

### Prerequisites
Make sure you have **Python 3.x** installed. The project also uses the **matplotlib** library for plotting. You can install it using:

```bash
pip install matplotlib
