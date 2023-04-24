def create_bytes_object() -> bytes:
    """
    Challenge #1 - Create a bytes object containing the byte values 0x41, 0x42 and 0x43 (which represent
    the ASCII characters 'A', 'B' and 'C'). Print the bytes object
    """

    bytes_obj = b"\x41\x42\x43"
    print(bytes_obj)
    return bytes_obj


def convert_bytes_to_string():
    """
    Challenge #2 - Convert the bytes object you created in Challenge #1 to a string using the UTF-8
    encoding. Print the resulting string
    """
    bytes_obj = b"\x41\x42\x43"
    print(bytes_obj.decode())


def read_file_as_bytes():
    """
    Challenge #3 - Open a file in binary mode and read its contents as bytes. Print the first 10 bytes
    of the file
    """
    with open("./challenge_3.txt", "rb") as file:
        print(file.read(10))


def manipulate_bytes():
    """
    Challenge #4 - Create a bytes object containing the byte values 0x00, 0x01, 0x02. Use slicing to
    create a new bytes object containing only the second and third bytes (0x01 and 0x02). Then, use
    the bitwise OR to set the second byte to 0xFF. Print the new bytes object
    """
    bytes_obj = b"\x00\x01\x02"
    new_bytes_object = bytearray(bytes_obj[1:3])
    new_bytes_object[1] |= 0xFF
    print(new_bytes_object)


if __name__ == "__main__":
    print("Challenge #1:")
    create_bytes_object()

    print("Challenge #2:")
    convert_bytes_to_string()

    print("Challenge #3:")
    read_file_as_bytes()

    print("Challenge #4:")
    manipulate_bytes()
