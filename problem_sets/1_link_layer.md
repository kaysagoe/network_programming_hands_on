# The Link Layer

This problem set contains exercises to understand the how data is sent and received using the link-layer protocols and how network applications are built using this layer

## 1.1 Mac Addresses

Create `utils` module containing 3 functions:

1. A function generates and returns a random MAC address in binary format
2. A function that takes a MAC address in binary format as input and returns the hexadecimal representation of the MAC address
3. A function takes a MAC address in string format and returns the binary representation of the MAC address

## 1.2 Ethernet Client and Server

Create the following:

1. A program that sends an ethernet frame to a given source and destination MAC address and a payload
2. A program that captures ethernet frames on a given network interface and prints out the source and destination of each frame
