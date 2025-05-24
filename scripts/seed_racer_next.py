import can
import time
import argparse

# Function to create CAN messages
def create_can_message(arbitration_id, data):
    return can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=True)

def main(send_id, receive_id, seed):
    # Create a CAN bus instance
    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=500000)

    # Response message data for the seed
    seed_response_data = [0x67, 0x01] + seed

    try:
        while True:
            # Listen for incoming messages
            message = bus.recv(timeout=1)

            if message and message.arbitration_id == receive_id:
                # Check if the message is a security access request (0x27 0x01)
                if message.data[:2] == [0x27, 0x01]:
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
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='CAN Security Access Script')
    parser.add_argument('--send_id', type=lambda x: int(x, 0), required=True, help='CAN ID to send responses to')
    parser.add_argument('--receive_id', type=lambda x: int(x, 0), required=True, help='CAN ID to listen for requests')
    parser.add_argument('--seed', type=lambda x: [int(i, 0) for i in x.split(',')], required=True, help='Seed value to send as response, comma separated')

    args = parser.parse_args()

    # Run the main function with provided arguments
    main(args.send_id, args.receive_id, args.seed)

