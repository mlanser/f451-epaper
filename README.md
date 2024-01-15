# f451 Labs E-Paper module v0.0.0

## Overview

The *f451 Labs E-Paper* module encapsulates the drivers for the [*Waveshare 2.7" e-ink display*](https://www.waveshare.com/product/displays/e-paper/epaper-2/2.7inch-e-paper-hat.htm?___SID=U) within a single class. This module also provides a standard set of methods to read sensor data and display content to the onboard 264x176 e-ink display.

## Install

This module is not (yet) available on PyPi. However, you can still use `pip` to install the module directly from GitHub (see below).

### Dependencies

This module is dependent on the following libraries:

- [Waveshare Python libraries](https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT_Manual#Python)

NOTE: Only install Waveshare libraries on a device that also has the physical Waveshare e-ink display installed.

NOTE: You can run this app in demo mode on (almost) any device even without the Waveshare e-ink display. It will then save the generated images to JPG files instead of displaying them.

NOTE: When log level is `DEBUG` or when `--debug` flag is used, the output will be saved as JPGs even when the e-ink display is present.

### Installing from GitHub using `pip`

You can use `pip install` to install this module directly from GitHub as follows:

Using HTTPS:

```bash
$ pip install 'f451-epaper @ git+https://github.com/mlanser/f451-epaper.git'
```

Using SSH:

```bash
$ pip install 'f451-epaper @ git+ssh://git@github.com:mlanser/f451-epaper.git'
```

## TODO How to use

### TODO Waveshare E-Ink Device

The `SenseHat` object makes it easy to interact with the Sense HAT device. The methods of this object help read sensor data, display data to the 8x8 LED, etc., and using the module is straightforward. Simply `import` it into your code and instantiate an `SenseHat` object which you can then use throughout your code.

```Python
# Import f451 Labs SenseHat
from f451_epaper.epaper import SenseHat

# Initialize device instance which includes all sensors
# and LED display on Sense HAT
mySense = SenseHat({
    "ROTATION": 0,
    "DISPLAY": 0,
    "PROGRESS": 0,
    "SLEEP": 600    
})

print(f"TEMP:     {round(mySense.get_temperature(), 1)} C")
print(f"PRESSURE: {round(mySense.get_pressure(), 1)} hPa")
print(f"HUMIDITY: {round(mySense.get_humidity(), 1)} %")
```

## TODOHow to test

The tests are written for [pytest](https://docs.pytest.org/en/7.1.x/contents.html) and we use markers to separate out tests that require the actual Sense HAT hardware. Some tests do not rely on the hardware to be present. However, those tests rely on the `pytest-mock` module to be present.

```bash

# Run all tests (except marked 'skip')
$ pytest

# Run tests with 'hardware' marker
$ pytest -m "hardware"

# Run tests without 'hardware' marker
$ pytest -m "not hardware"
```
