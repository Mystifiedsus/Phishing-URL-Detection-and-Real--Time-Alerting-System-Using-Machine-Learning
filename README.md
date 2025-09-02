IoT Device Security Simulation
This project is a Python-based simulation demonstrating a simple authentication protocol for IoT devices and its vulnerability to common cyberattacks. It provides a foundational understanding of how replay, data injection, and denial-of-service (DoS) attacks can affect a network of IoT devices and how an authentication protocol can mitigate some of these threats.

Table of Contents
Features

How to Run

Code Structure

License

Features
Simulated IoT Devices: Creates and manages multiple IoT devices that can send authenticated messages.

Authentication Protocol: Implements a simple shared-key authentication scheme to verify message integrity and origin.

Attack Simulation: Includes classes to simulate three major types of attacks:

Replay Attack: Re-sends a previously valid message to the server.

Data Injection Attack: Modifies the content of a valid message to inject malicious data.

Denial-of-Service (DoS) Attack: Simulates network congestion by dropping a percentage of messages.

Performance Metrics: Evaluates and reports key performance metrics such as latency, energy consumption, and authentication success rate.

Data Visualization: Generates and saves plots to visualize key metrics, providing a clear summary of the simulation results.

How to Run
Prerequisites
Make sure you have Python installed. The project also uses the matplotlib library for plotting. You can install it using pip.

Bash

pip install matplotlib
Execution
Simply run the main script from your terminal.

Bash

python main.py
The script will print the results of the different simulations to the console and save two image files, latency_energy_plot.png and auth_success_rate.png, in the same directory.

Code Structure
.
├── auth_protocol.py
├── attacks.py
├── device.py
├── main.py
├── metrics.py
└── utils.py
main.py: The main script that orchestrates the simulation. It initializes the devices and server, runs the attack simulations, calculates the metrics, and generates the plots.

auth_protocol.py: Defines the AuthProtocol class, which handles the authentication logic using a shared key.

attacks.py: Implements the AttackSimulator class with methods for running replay, data injection, and DoS attacks.

device.py: Defines the IoTDevice class, representing a simulated device.

metrics.py: Defines the Metrics class for calculating and evaluating performance and security metrics.

utils.py: Includes utility functions, such as print_message_report to format and display message information.

License
This project is open-source and available under the MIT License.
