import wave
import pyaudio
import numpy
import socket
import struct

LED_DRIVER_HOST = '0.0.0.0'  #Set this to the address of the raspberry pi with the LEDs attached
#LED_DRIVER_HOST = 'localhost'
LED_DRIVER_PORT = 50007
BUFFER_SIZE = 512


def main():
    display_buffer = [bytearray([0x00, 0x00, 0x00]) for i in xrange(36)]

    #input_stream = FileReader('8k8bitpcm.wav')  # local file for testing
    input_stream = LiveReader()
    output_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def lpush(buffer, byte):
        def lpush_iter(buffer, pos, byte):
            if pos < len(buffer):
                current_byte = buffer[pos]
                buffer[pos] = byte
                return lpush_iter(buffer, pos+1, current_byte)
            else:
                return buffer

        return lpush_iter(buffer, 0, byte)

    audio_bytes = input_stream.read_bytes(BUFFER_SIZE)

    while audio_bytes:
        buf = numpy.frombuffer(audio_bytes, dtype=numpy.int8)
        window = numpy.hanning(len(buf))
        buf = buf * window
        fourier = numpy.fft.rfft(buf, 8)

        power = numpy.abs(fourier)
        spectrum = (power * 255/power.max()).astype(numpy.int8).clip(0)
        element = bytearray([spectrum[1], spectrum[2], spectrum[3]])

        display_buffer = lpush(display_buffer, element)
        buf = ""
        for pixel in display_buffer:
            buf += struct.pack('BBB', *pixel)
        output_socket.sendto(
            buf,
            (LED_DRIVER_HOST, LED_DRIVER_PORT)
        )
        audio_bytes = input_stream.read_bytes(BUFFER_SIZE)


class AudioReader(object):
    def read_bytes(self, buffer_size):
        pass


class FileReader(AudioReader):
    def __init__(self, file_name):
        self._fp = wave.open(file_name, 'r')

    def read_bytes(self, buffer_size):
        return self._fp.readframes(buffer_size)


class LiveReader(AudioReader):
    def __init__(self):
        self._paudio = pyaudio.PyAudio()
        self._stream = self._paudio.open(
            format=pyaudio.paInt8,
            channels=1,
            rate=16000,
            input=True
        )

    def read_bytes(self, buffer_size):
        return self._stream.read(buffer_size)

main()