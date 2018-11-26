### List of packet which is ready to use in in python-broadlink to control devices via Broadlink RM Pro IR/RF.

### How to get that packet
- You should have a Broadlink device
- Using great python module broadlink (from mjg58)

### Learning code
```python
import broadlink
devices = broadlink.discover(timeout=10)
print 'Authentication status {}'.format (devices[0].auth())

# FOR LEARNING
print 'Start learning'
devices[0].enter_learning()

print 'Learned code in byte array'
bytearray(devices[0].check_data())

```
Then share your packet.
In this repo i shared my Samsung TV's IR packet code, in byte array.

### Built-in Temperature sensor
```python
devices[0].check_temperature()
```

### Share your packet
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

