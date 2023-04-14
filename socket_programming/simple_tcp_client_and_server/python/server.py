import sys
import logging
from socket import AF_INET, SOCK_STREAM, socket

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def run_server(port: int) -> None:
    logging.info("Server started")
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", port))
        sock.listen(10)

        try:
            while True:
                conn, addr = sock.accept()
                logging.info(f"Received connection from {addr}")

                conn.send(f"Hello, {addr[0]}:{addr[1]}".encode())
                conn.close()
                logging.info(f"Closed connection from {addr}")
        except KeyboardInterrupt:
            logging.info("Closing server")


if __name__ == "__main__":
    port = int(sys.argv[1])
    run_server(port)
