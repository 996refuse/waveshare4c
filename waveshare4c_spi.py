#!/usr/bin/env python2

import spidev
import RPi.GPIO as GPIO

__author__ = "letli"

class Display:
	def __init__(self, rs, dc):
		self.spi = spidev.SpiDev()
		self.spi.open(0, 0)
		self.spi.max_speed_hz = 125000

		self.rs = rs
		self.dc = dc

		GPIO.setmode(GPIO.BCM)
		GPIO.setup([self.rs, self.dc], GPIO.OUT)
		
		GPIO.output(self.rs, GPIO.HIGH)
		GPIO.output(self.rs, GPIO.LOW)
		GPIO.output(self.rs, GPIO.HIGH)

		self.set_color(0, 0, 0)

	def __exit__(self, type, value, trace):
		self.spi.close()
		GPIO.cleanup([self.rs, self.dc])

	def __enter__(self):
		return self

	def iterator_8bit(self, seq_16bit_word):
		for word in seq_16bit_word:
			yield (word >> 8) & 0xFF
			yield  word       & 0xFF

	def command(self, *args):
		args = list(args)
		GPIO.output(self.dc, GPIO.LOW)
		self.spi.xfer3(list(self.iterator_8bit(args[:1])))

		GPIO.output(self.dc, GPIO.HIGH)
		if args[1:]:
			self.spi.xfer3(list(self.iterator_8bit(args[1:])), 125000000 )

	def set_color(self, r, g, b):
		r = min(r, 0x1F) << 11
		g = min(g, 0x3F) << 5
		b = min(b, 0x1F)
		self._color = r | g | b

	def draw_pixel(self, x, y):
		self.command(0x2A, x >> 8, x & 0xFF, x >> 8, x & 0xFF)
		self.command(0x2B, y >> 8, y & 0xFF, y >> 8, y & 0xFF)
		self.command(0x2C, self._color)

	def init(self, seq):
		i = 0
		while i < len(seq):
			if seq[i] == -1:
				i += 1
				j = i
				while seq[i] >= 0:
					i += 1
				self.command(*seq[j:i])
			elif seq[i] == -2:
				i += 1
				time.sleep(seq[i] / 1000)
				i += 1
			elif seq[i] == -3:
				return

if __name__ == '__main__':
	from const import waveshare4c_init
	from time import sleep
	from font import Font

	RS = 25
	DC = 24
	with Display(RS, DC) as d:
		d.init(waveshare4c_init)

		io = Font(d)
		io.printf("fuck world\n", 30, 80)

		while (True):
			sleep(10)
