import broadlink
devices = broadlink.discover(timeout=10)
print 'Authentication status {}'.format (devices[0].auth())

# FOR LEARNING
print 'Start learning'
devices[0].enter_learning()

print 'Learned code in byte array'
bytearray(devices[0].check_data())
