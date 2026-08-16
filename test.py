import struct, sys
with open(sys.argv[1], 'rb') as f:
  data = f.read()
pos = 0
ctype, csize, cver = struct.unpack('<III', data[pos:pos+12])
pos += 12
while pos < len(data) - 12:
  c, s, v = struct.unpack('<III', data[pos:pos+12])
  if c == 0x15:
    c2, s2, v2 = struct.unpack('<III', data[pos+12:pos+24])
    if c2 == 0x01:
      p2 = pos + 24
      plat, filt = struct.unpack('<II', data[p2:p2+8])
      name = data[p2+8:p2+40].split(b'\x00')[0].decode('ascii')
      rfmt, dfmt, w, h, d = struct.unpack('<IIHHB', data[p2+72:p2+85])
      print(f'{name}: {w}x{h}, depth={d}, format=0x{rfmt:X}')
  pos += s + 12
