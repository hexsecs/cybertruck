import can

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
print("Listening for messages...")
for msg in bus:
    print(msg)

