def clear_seq():
	color = 0xBB00
	seq = [
		-1, 0x2A, 0 >> 8, 0 & 0xFF, 480 >> 8, 480 & 0xFF,
		-1, 0x2B, 0 >> 8, 0 & 0xFF, 320 >> 8, 320 & 0xFF,
		-1, 0x2C
	]
	return seq + [color] * 320 * 480

init = [
	-1, 0xF0, 0xC3,
	-1, 0xF0, 0x96,
	-1, 0x36, 0x68,
	-1, 0x3A, 0x05,
	-1, 0xB0, 0x80,
	-1, 0xB6, 0x20, 0x02,
	-1, 0xB5, 0x02, 0x02, 0x00, 0x04,
	-1, 0xB1, 0x80, 0x10,
	-1, 0xB4, 0x00,
	-1, 0xB7, 0xC6,
	-1, 0xC5, 0x5D,
	-1, 0xE4, 0x31,
	-1, 0xE8, 0x40, 0x8A, 0x00, 0x00, 0x29, 0x19, 0xA5, 0x33,
	-1, 0xC2,
	-1, 0xA7,
	-1, 0xE0, 0xF0, 0x09, 0x13, 0x12, 0x12, 0x2B, 0x3C, 0x44, 0x4B, 0x1B, 0x18, 0x17, 0x1D, 0x21,
	-1, 0xE1, 0xF0, 0x09, 0x13, 0x0C, 0x0D, 0x27, 0x3B, 0x44, 0x4D, 0x0B, 0x17, 0x17, 0x1D, 0x21,
	-1, 0x36, 0xEC,
	-1, 0xF0, 0x3C,
	-1, 0xF0, 0x69,
	-1, 0x13,
	-1, 0x11,
	-1, 0x29,
]

clear = clear_seq()
end = [-3]

waveshare4c_init = init + clear + end