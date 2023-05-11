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


def interface_exists(name: str) -> bool:
    if name not in [name_index[1] for name_index in socket.if_nameindex()]:
        return False
    return True


def create_ether_sock(interface: str) -> Tuple[socket.socket, bytes]:
    if not interface_exists(interface):
        raise Exception(f"Interface {interface} does not exist in the host")

    with open(f"/sys/class/net/{interface}/address", "rb") as address_file:
        mac = mac_hex_to_bin(address_file.read())

    sock_fd = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x88B6))  # type: ignore
    sock_fd.bind((interface, 0))

    return sock_fd, mac


def send_frame(sock_fd: socket.socket, host_mac: bytes, dest_mac: bytes, payload: str):
    payload_bin = payload.encode("ascii")
    length = (14 + len(payload_bin)).to_bytes(2)
    data = host_mac + dest_mac + b"\x88\xB6" + length + payload.encode("ascii")
    sock_fd.sendall(data)


def read_frame(sock_fd: socket.socket, read_buffer: bytes) -> Tuple[Frame, bytes]:
    if len(read_buffer) < 16:
        read_buffer = _read_to_buffer(read_buffer, sock_fd)

    host_mac, read_buffer = _get_bytes_from_buffer(read_buffer, 6)
    dest_mac, read_buffer = _get_bytes_from_buffer(read_buffer, 6)
    ether_type, read_buffer = _get_bytes_from_buffer(read_buffer, 2)
    length, read_buffer = _get_bytes_from_buffer(read_buffer, 2)
    length_int = int.from_bytes(length)

    if len(read_buffer) < length_int:
        read_buffer = _read_to_buffer(read_buffer, sock_fd)
    payload, read_buffer = _get_bytes_from_buffer(read_buffer, length_int - 16)
    return Frame(host_mac, dest_mac, length_int, payload), read_buffer


def _get_bytes_from_buffer(buffer: bytes, length: int) -> Tuple[bytes, bytes]:
    return buffer[:length], buffer[length:]


def _read_to_buffer(buffer: bytes, sock_fd: socket.socket) -> bytes:
    return buffer + sock_fd.recv(1024)
