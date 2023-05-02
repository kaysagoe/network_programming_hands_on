from random import choices
from binascii import unhexlify, hexlify


def mac_hex_to_bin(address: bytes) -> bytes:
    add_without_sep = address.replace(b":", b"")

    if len(add_without_sep) != 12:
        raise ValueError(
            "The hexadecimal representation of the MAC address has to contain 12 characters"
        )

    return unhexlify(add_without_sep)


def mac_bin_to_hex(address: bytes, byte_delimiter: bool) -> bytes:
    if len(address) != 6:
        raise ValueError("The MAC address must contain 6 bytes")

    if byte_delimiter:
        return hexlify(address, b":", 1)
    else:
        return hexlify(address)


def generate_mac() -> bytes:
    mac_str = "".join(
        choices(
            [str(char) for char in range(0, 10)] + ["a", "b", "c", "d", "e", "f"], k=12
        )
    )
    return bytes(mac_str, "ascii")


if __name__ == "__main__":
    mac = generate_mac()
    print(f"The generated MAC address in hexadecimal format is:")
    print(mac)

    mac_bin = mac_hex_to_bin(mac)
    print("The mac address in binary format is:")
    print(mac_bin)

    print("The mac address back to hexadecimal format is:")
    print(mac_bin_to_hex(mac_bin, True))
