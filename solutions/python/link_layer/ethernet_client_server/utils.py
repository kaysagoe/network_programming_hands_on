import socket
from typing import Tuple
from link_layer.mac_addresses.utils import mac_hex_to_bin
from dataclasses import dataclass


@dataclass
class Frame:
    host_mac: bytes
    dest_mac: bytes
    length: int
    payload: bytes


def create_ether_sock(interface: str) -> Tuple[socket.socket, bytes]:
    if interface not in [name_index[1] for name_index in socket.if_nameindex()]:
        raise Exception(f"Interface {interface} does not exist in the host")

    with open(f"/sys/class/net/{interface}/address", "rb") as address_file:
        mac = mac_hex_to_bin(address_file.read())

    sock_fd = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)  # type: ignore
    sock_fd.bind((interface, 0))

    return sock_fd, mac


def send_frame(sock_fd: socket.socket, host_mac: bytes, dest_mac: bytes, payload: str):
    payload_bin = payload.encode("ascii")
    length = (14 + len(payload_bin)).to_bytes(2)
    data = host_mac + dest_mac + length + payload.encode("ascii")
    sock_fd.sendall(data)


def read_frame(sock_fd: socket.socket, read_buffer: bytes) -> Tuple[Frame, bytes]:
    if len(read_buffer) >= 14:
        host_mac, read_buffer = _get_bytes_from_buffer(read_buffer, 6)
        dest_mac, read_buffer = _get_bytes_from_buffer(read_buffer, 6)
        length, read_buffer = _get_bytes_from_buffer(read_buffer, 2)
        length_int = int.from_bytes(length)
    if len(read_buffer) < length_int:
        read_buffer = read_buffer + sock_fd.recv(1024)
    payload, read_buffer = _get_bytes_from_buffer(read_buffer, length_int - 14)
    return Frame(host_mac, dest_mac, length_int, payload), read_buffer


def _get_bytes_from_buffer(buffer: bytes, length: int) -> Tuple[bytes, bytes]:
    return buffer[:length], buffer[length:]
