# Broadlink_RM_Pro_ControlCode
### List of code which is ready to use in in python broadlink

### How to get that code
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
Then share your code!
