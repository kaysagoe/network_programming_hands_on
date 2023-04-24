# Working with Bytes

Raw bytes are used a lot, all over network programming. Most of the messages exchanged in computer networks are in byte format.
This is a preparation problem set to get acquainted with manipulating bytes in different programming languages.

It contains four challanges:

1. Create a bytes object containing the byte values 0x41, 0x42, and 0x43 (which represent the ASCII characters 'A', 'B', and 'C'). Print the bytes object.
2. Convert the bytes object you created in Challenge #1 to a string using the UTF-8 encoding. Print the resulting string.
3. Open a file in binary mode and read its contents as bytes. Print the first 10 bytes of the file.
4. Create a bytes object containing the byte values 0x00, 0x01, and 0x02. Use slicing to create a new bytes object containing only the second and third bytes (0x01 and 0x02). Then, use bitwise OR to set the second byte to 0xFF. Print the new bytes object.
