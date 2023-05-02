from utils import create_ether_sock, send_frame
from link_layer.mac_addresses.utils import mac_hex_to_bin


def main():
    while True:
        print("Send an Ethernet Frame")

        interface = input("Network Interface Name: ")
        dest_mac = mac_hex_to_bin(input("Destination MAC Address: "))
        payload = input("Payload: ")

        sock_fd, host_mac = create_ether_sock(interface)
        send_frame(sock_fd, host_mac, dest_mac, payload)
        print("Frame sent")


if __name__ == "__main__":
    main()
