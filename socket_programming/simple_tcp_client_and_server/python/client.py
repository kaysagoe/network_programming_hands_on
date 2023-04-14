import logging
import sys
from socket import socket, AF_INET, SOCK_STREAM

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def run_client(ip: str, port: int) -> None:
    logging.info("Client started")
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect((ip, port))
        logging.info(f"Connected to server {ip}:{port}")

        data = b""

        while data == b"":
            data = sock.recv(1024)

        logging.info(data.decode())
        logging.info(f"Closing connection to server {ip}:{port}")
    logging.info("Stopping client")


if __name__ == "__main__":
    ip = sys.argv[1]
    port = int(sys.argv[2])
    run_client(ip, port)
