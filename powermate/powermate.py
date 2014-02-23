import usb.core

dev = usb.core.find()
dev.set_configuration()
dev.detach_kernel_driver()

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
