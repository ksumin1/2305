with open('binary.bin', 'wb') as f:
    # data = b'\xea\xb0\x80'
    data = bytes([255, 0, 127])
    f.write(data)