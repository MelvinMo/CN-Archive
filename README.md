# CN-Archive

## Project 1: Implementing a Basic FTP Client and Server

This project involved developing a basic FTP client in Python that could connect to an FTP server and transfer files.

The key aspects were:
- Implemented socket programming in Python to enable communication between client and server over TCP/IP
- Utilized the FTP protocol, which operates over TCP like HTTP.
- Developed an FTP client that can connect to a server, send commands like LIST to get a file listing, DWLD to download a file, PWD to print the working directory, etc.
- Handled errors such as "file not found" and bad requests in a graceful manner by sending appropriate replies to the server
- Tested the client by transferring files of different sizes between the client and a server running on localhost
- Analyzed the TCP handshake, packets transferred, and control vs data connections using Wireshark
- Documented the project with screenshots demonstrating the FTP session between client and server

## Project 2: Analysis of Transport Layer Protocols (TCP and UDP)

This project involved studying the impact of network conditions like delay, loss, and bandwidth on TCP and UDP protocol performance.

The key aspects were:
- Used network emulation tool tc and iperf to generate different network scenarios like added delay, loss, and bandwidth variations
- Measured throughput over TCP and UDP under different conditions using iperf
- Captured packets exchanged between client and server for both TCP and UDP using Wireshark
- Analyzed TCP handshakes, data packets, and retransmissions under different conditions
- Compared throughput values and retransmissions for TCP under different network scenarios
- Observed lack of feedback and error correction in UDP compared to TCP
- Documented observations on TCP vs UDP performance and behavior under different network conditions

<p align="center">
  <img src="https://github.com/MelvinMo/CN-Archive/blob/main/Project%202/Pictures/TCP/TCP%20-%20Ideal/Graph%20-%20Ideal.png" alt="IMG" />
</p>
