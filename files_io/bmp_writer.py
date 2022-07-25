"""A module for dealing with BMP bitmap image files"""


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file

    Args:
        filename: The name of the BMP file to created
        pixels: A rectangular image stored as a sequence of rows.
                Each row must be an iterable series of integers in the range of 0-255
    Raises:
        ValueError: If any of the integer is out of range
        OSError: If the file could not be written

    Note:
        BMP format is a little endian
    """

    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        bmp.write(b'BM')  # bmp header format, identify as BMP file

        size_bookmark = bmp.tell()  # the next four bytes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  # little endian integer. Zero placeholder for now
        # least significant bytes is written first

        bmp.write(b'\x00\x00')  # unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')  # unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell()  # the next four bytes hold the integer offset to the
        # pixel data, zero-placeholder for now
        bmp.write(b'\x00\x00\x00\x00')

        # image header
        bmp.write(b'\x28\x00\x00\x00')  # imgea header size in bytes - 40 decimal
        # as 32-bit integer, in this case it is 40-bytes long
        # hardwired as a hexadecimal
        bmp.write(_int32_to_bytes(width))  # image width in pixels
        bmp.write(_int32_to_bytes(height))  # image height in pixels

        # below are standard fixed for 8-but grayscale image header
        bmp.write(b'\x01\x00')  # number of image planes
        bmp.write(b'\x08\x00')  # bits per pixel 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00')  # no compression
        bmp.write(b'\x00\x00\x00\x00')  # zero for uncompressed image
        bmp.write(b'\x00\x00\x00\x00')  # unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # use whole color table
        bmp.write(b'\x00\x00\x00\x00')  # all colors are important

        # color palette - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))  # Blue, Green, Red, Zero

        # pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):  # BMP files are bottom to top
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * ((4 - (len(row) % 4)) % 4)  # pad row to multiple of four bytes
            bmp.write(padding)

        # end of file
        eof_bookmark = bmp.tell()

        # fill in the file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # fill in pixel
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""

    # &: bitwise-and
    # >> : right-shift

    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))
