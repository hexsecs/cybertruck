import can

bus = can.interface.Bus(channel = 'PCAN_USBBUS1', interface='pcan', bitrate=500000)
print("Connected to PEAK CAN device")

can_id = 0x0CF00331
data = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]
message = can.Message(arbitration_id=can_id, data=data, is_extended_id=True)

bus.send(message)
