import can
import time
import binascii

# Function to create CAN messages
def create_can_message(arbitration_id, data):
    return can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=True)

def main():
    # Create a CAN bus instance
    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=500000)

    # CAN IDs for sending and receiving messages
    receive_id = 0x18DA03F9
    send_id = 0x18DAF903

    # Response message data for the seed (0xFF 0xFF)
    seed_response_data = [0x04, 0x67, 0x01, 0x12, 0x38, 0xAA, 0xAA, 0xAA]

    try:
        while True:
            # Listen for incoming messages
            message = bus.recv(timeout=1)

            if message and message.arbitration_id == receive_id:
                # Check if the message is a security access request (0x27 0x01)
                if message.data[:3] == b"\x02\x27\x01":
                    #print( hex(message.data))
                    hex_string = binascii.hexlify(message.data).decode('utf-8').upper()
                    print(hex_string)
                    b_array = binascii.unhexlify(hex_string)
                    print(b_array)
                    print(f"Received security access request: {message}")

                    # Send the seed response
                    seed_response_msg = create_can_message(send_id, seed_response_data)
                    bus.send(seed_response_msg)
                    print(f"Sent seed response: {seed_response_msg}")

    except KeyboardInterrupt:
        print("Script interrupted by user.")

    finally:
        # Clean up the bus
        bus.shutdown()

if __name__ == "__main__":
    main()

