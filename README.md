# waveshare4c

waveshare 4inch RPi LCD (C) python driver

dependency
------------

[RPi.GPIO](https://sourceforge.net/projects/raspberry-gpio-python/)
[spidev](https://pypi.org/project/spidev/)

chip
------------

ili9486 for screen

xpt2046 for touch

pinout
------------

to control the display screen, at least 5 pins are required, namely
```
GPIO      RPI B+ Pin Number

GPIO_8    24                  CE0
GPIO_10   19                  MOSI
GPIO_11   23                  SCLK
GPIO_24   18                  DC
GPIO_25   22                  RS
```

todo
------------

touch driver

product page
------------

https://www.waveshare.com/wiki/4inch_RPi_LCD_(C)
  
http://www.waveshare.net/w/index.php?title=4inch_RPi_LCD_(C)
