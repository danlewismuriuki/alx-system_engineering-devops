# OSI Model and Networking Essentials

## OSI Model Overview
The OSI (Open Systems Interconnection) model is a conceptual framework that defines seven abstraction layers to facilitate understanding and describing network protocols and communication over a network. Each layer is responsible for specific functions and interactions with adjacent layers.

### Layers of the OSI Model
1. **Physical Layer**: Deals with the physical connection between devices and transmission of raw data bits over a communication channel.
2. **Data Link Layer**: Provides error detection and correction, framing of data packets, and logical addressing (MAC addresses).
3. **Network Layer**: Handles routing, forwarding, and addressing to facilitate communication between devices across different networks. IP operates at this layer.
4. **Transport Layer**: Ensures reliable end-to-end communication by segmenting data, handling flow control, error correction, and congestion control. TCP and UDP operate here.
5. **Session Layer**: Establishes, maintains, and terminates communication sessions between applications.
6. **Presentation Layer**: Translates data between the application layer and the network format, handling encryption, compression, and conversion.
7. **Application Layer**: Provides network services directly to end-users and applications.

## LAN (Local Area Network)
- **What it is**: Connects devices within a limited geographic area like a home, office, or campus.
- **Typical usage**: Facilitates communication and resource sharing among devices within a small area.
- **Typical geographical size**: Covers small areas like a single building or campus.

## WAN (Wide Area Network)
- **What it is**: Connects devices over large geographic areas, spanning cities, countries, or continents.
- **Typical usage**: Connects LANs to facilitate communication between devices across long distances.
- **Typical geographical size**: Spans large geographic areas potentially across vast distances.

## Internet
- **What it is**: Global network of interconnected computers and networks using standardized protocols.
- **Typical usage**: Used for various purposes like accessing websites, sending emails, downloading files, and more.
- **Typical geographical size**: Spans the entire globe, connecting devices and networks worldwide.

## IP Address
- **What it is**: Unique numerical identifier assigned to each device connected to a network using IP.
- **Types**: IPv4 (32-bit) and IPv6 (128-bit).

## localhost
- **What it is**: Refers to the loopback network interface of a device, typically identified by the IP address 127.0.0.1.
  
## Subnet
- **What it is**: Logical subdivision of an IP network for organizational or security purposes.

## Reasons for IPv6
- **Why IPv6 was created**: Due to the exhaustion of available IPv4 addresses, IPv6 provides a larger address space, improved network security, auto-configuration, and support for new technologies.

## TCP/UDP
- **Mainly used data transfer protocols for IP**: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
- **Main difference**: TCP is connection-oriented and provides reliable, ordered delivery, while UDP is connectionless and prioritizes speed over reliability.

## Port
- **What it is**: Logical endpoint for communication in an operating system.
- **Port numbers**:
  - SSH: Port 22
  - HTTP: Port 80
  - HTTPS: Port 443

## Tool/Protocol for Network Connectivity
- **Tool/protocol used**: ICMP (Internet Control Message Protocol), specifically the "ping" command.
