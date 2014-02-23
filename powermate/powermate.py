import usb.core

PULSE_MODE_DIVIDE = 0
PULSE_MODE_NORMAL = 1
PULSE_MODE_MULTIPLY = 2

class PowerMate(object):
    def __init__(self):
        self.dev = usb.core.find(idVendor=0x077d, idProduct=0x0410)
        if dev == None:
            raise Exception("Could not find the PowerMate")

        self.dev.set_configuration()
        
        if self.dev.is_kernel_driver_active(0):
            self.dev.detach_kernel_driver(0)

    def set_brightness(self, brightness):
        """Sets the brightness of the PowerMate's LED
             brightness: A value from 0 (darkest) to 255 (brightest), inclusive
        """
        dev.ctrl_transfer(0x41, 0x01, 0x01, brightness, [], timeout=0)

    def set_pulse(pulse):
        """Sets whether or not to pulse constantly
             pulse: A boolean value indicating whether to pulse (True), or not
             (False)
        """
        dev.ctrl_transfer(0x41, 0x01, 0x03, int(pulse), [], timeout=99999999)

    def set_pulse_asleep(pulse):
        """Sets whether or not to pulse when the computer is asleep
             pulse: A boolean value indicating whether to pulse (True), or not
             (False)
        """
        dev.ctrl_transfer(0x41, 0x01, 0x02, 0, [], timeout=99999999)

    def set_pulse_speed(speed)
        """Sets the pulse speed of the PowerMate's LED
             speed: A value from -255 to 255 (inclusive). Lower values are
               slower, higher values are faster
        """
        if speed < 0:
            mode = 0
            speed = -speed
        elif speed == 0:
            mode = 1
        elif speed > 0:
            mode = 2
        wValue = (mode << 8) | 0x04 # Compute value: 0x04 is SET_PULSE_MODE command
        wIndex = (speed << 8) | mode

        # Set pulse mode
        dev.ctrl_transfer(0x41, 0x01, wValue, wIndex, [], timeout=0)


dev.read(129, 6, timeout=99999999999) # endpoint address, length

brightness = 255

# Set brightness
dev.ctrl_transfer(0x41, 0x01, 0x01, brightness, [], timeout=0) # wValue and wIndex are important

# Set pulse awake
dev.ctrl_transfer(0x41, 0x01, 0x03, 0, [], timeout=99999999) # 0 for off, 1 for on

# Set pulse asleep
dev.ctrl_transfer(0x41, 0x01, 0x02, 0, [], timeout=99999999) 

pulse_mode = 1 # Can be 0, 1, or 2

wValue = (pulse_mode << 8) | 0x04 # Compute value: 0x04 is SET_PULSE_MODE command
effect = 255 # Maximum effect, from 0 to 255
wIndex = (effect << 8) | pulse_mode

# Set pulse mode
dev.ctrl_transfer(0x41, 0x01, wValue, wIndex, [], timeout=99999999)

""" dev.read return value:
    Array:
    0: Button position (0 is not pressed, 1 is pressed)
    1: Amount turned (positive 1, 2, 3 etc for right, negative 1 (255), 2, 3
    etc for left
    2: 0 (meaningless)
    3: Static brightness (0-255)
    4: LED status (pulsing or constant brightness, pulse while sleep)
    5: Pulse value (0-255)
"""
