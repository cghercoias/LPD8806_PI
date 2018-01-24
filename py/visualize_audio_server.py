import socket
import struct
from raspledstrip.LPD8806 import LPD8806SPI
led_strip = LPD8806SPI(36)

HOST = ''
PORT = 50007

input_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
input_socket.bind((HOST, PORT))
display_buffer = [bytearray([0x00, 0x00, 0x00]) for i in xrange(36)]
gamma = [0x80 | int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5) for i in range(256)]


def lpush(buffer, byte):
    def lpush_iter(buffer, pos, byte):
        if pos < len(buffer):
            current_byte = buffer[pos]
            buffer[pos] = byte
            return lpush_iter(buffer, pos+1, current_byte)
        else:
            return buffer

    return lpush_iter(buffer, 0, byte)


while 1:
    byte_buffer, from_addr = input_socket.recvfrom(36*3)
    for i in xrange(36):
        pixel = struct.unpack('BBB', byte_buffer[i*3:(i*3 + 3)])
        display_buffer = lpush(display_buffer, bytearray([gamma[pixel[0]], gamma[pixel[1]], gamma[pixel[2]]]))
    led_strip.update(display_buffer)
    #print display_buffer