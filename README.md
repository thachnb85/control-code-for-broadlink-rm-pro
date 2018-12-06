### List of packet which is ready to use in in python-broadlink to control devices via Broadlink RM Pro IR/RF.

### How to get that packet
- You should have a Broadlink device
- Using great python module broadlink (from mjg58)

### Learning code
```python
import broadlink
import binascii
import struct

devices = broadlink.discover(timeout=10)
print 'Authentication status {}'.format (devices[0].auth())

# Step: 1: Start Learning Mode
devices[0].enter_learning()
# At this point, you can see yellow led light ON on Broadlink device.

# Step 2: Now you should press button, if Broadlnk learned code successfully, yellow light will be off.

# Step 3: Make code ready for Home Asisstant
binascii.b2a_base64(bytearray(devices[0].check_data()))

```
### Built-in Temperature sensor
```python
devices[0].check_temperature()
```

### Send code using Broadlink
Example here 

```python
samsung_tv_power = b'&\x00\x8c\x00\x93\x91\x155\x145\x154\x15\x10\x15\x10\x15\x0f\x15\x10\x15\x10\x154\x154\x155\x15\x10\x14\x10\x15\x10\x15\x10\x14\x10\x15\x10\x154\x15\x10\x15\x10\x15\x0f\x15\x10\x15\x10\x15\x0f\x155\x15\x0f\x155\x154\x155\x154\x154\x155\x15\x00\x05\xf3\x94\x90\x155\x154\x155\x14\x10\x15\x10\x15\x10\x14\x10\x15\x10\x154\x155\x145\x15\x10\x15\x0f\x15\x10\x15\x10\x15\x0f\x15\x10\x154\x15\x10\x15\x10\x15\x10\x14\x10\x15\x10\x15\x10\x145\x15\x10\x145\x154\x155\x154\x155\x145\x15\x00\r\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

devices[0].send_data(str(samsung_tv_power))
```

### Credit
Thanks to mjg59 for great python-broadlink bridge
https://github.com/mjg59/python-broadlink

### License
MIT

