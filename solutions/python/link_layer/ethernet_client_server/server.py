import sys
from link_layer.mac_addresses.utils import mac_bin_to_hex
from utils import create_ether_sock, read_frame


def main():
    sock_fd = create_ether_sock(sys.argv[1])
    read_buffer = bytes()
    while data := read_frame(sock_fd, read_buffer):
        frame, read_buffer = data
        print("Received Frame")
        print(f"Source MAC Address: {mac_bin_to_hex(frame.host_mac, True)}")
        print(f"Destination MAC Address: {mac_bin_to_hex(frame.dest_mac, True)}")
        print(f"Payload: {frame.payload.decode('ascii')}")
        print()


if __name__ == "__main__":
    main()
