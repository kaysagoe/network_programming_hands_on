This programming exercise is designed to test your ability to create a TCP server that can listen for incoming connections and respond with a message. The goal is to create a server that can receive new connections from multiple clients and respond with a greeting message.

## Requirements

### Server

- The server should be able to listen for incoming connections on a specified TCP port.
- When the server receives a new connection from a client, it should respond with a message that includes the client's IP address. The message should be in the following format: "Hello, <IP_ADDRESS>".
- The server should be able to receive new connections from multiple clients one after the other.

### Client

- The client should be able to connect to an arbitrary TCP server.
- The client should be able to send and receive messages from the server.

## Usage

### Python

To run the Python version of the server, navigate to the python directory and run the following command:

```
poetry run python server.py <SERVER_PORT>
```

To run the Python version of the client, navigate to the python directory and run the following command:

```
poetry run python <SERVER_IP_ADDRESS> <SERVER_PORT>
```
