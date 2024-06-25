To set the default interface to using the `.canrc` configuration file for `python-can`, you need to create or edit the `.canrc` file in your home directory. Here is a step-by-step guide:

### Step 1: Create or Edit `.canrc`

Create a `.canrc` file in your home directory if it doesn't already exist, and configure it to use `vcan0` as the default interface.

```sh
nano ~/.canrc
```

Add the following content to the `.canrc` file:

```ini
[default]
interface = socketcan
channel = vcan0   # This could be can0 or whatever can interface you wish to use
bitrate = 500000
```

This configuration sets `socketcan` as the interface type, `vcan0` as the channel, and a bitrate of `500000`.

### Step 2: Python Script to Use the Configuration

Here's how you can create a Python script that uses the `vcan0` interface configured in `.canrc`:

```python
import can

def setup_can_interface():
    # Set up the CAN bus using the default interface set in .canrc
    can_bus = can.interface.Bus()
    return can_bus

def main():
    # Set up the CAN interface
    can_bus = setup_can_interface()

    # Example: Send a CAN message
    message = can.Message(arbitration_id=0x123, data=[0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88], is_extended_id=False)
    try:
        can_bus.send(message)
        print("Message sent on vcan0")
    except can.CanError:
        print("Message NOT sent")

    # Example: Receive a CAN message
    try:
        received_message = can_bus.recv(timeout=1.0)
        if received_message:
            print(f"Message received: {received_message}")
        else:
            print("No message received within timeout period")
    except can.CanError:
        print("Error receiving message")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **Setup CAN Interface:**
   - The `setup_can_interface` function initializes the CAN interface using the configuration specified in the `.canrc` file.

2. **Main Function:**
   - It sets up the CAN interface by calling `setup_can_interface`.
   - It sends a sample CAN message.
   - It receives a CAN message with a timeout of 1 second.

### Running the Script

After setting up the `vcan0` interface and configuring the `.canrc` file, you can run the Python script:

```sh
python your_script_name.py
```

Make sure to replace `your_script_name.py` with the actual name of your Python script file.

This example sets `python-can` to use `vcan0` as the default CAN interface based on the `.canrc` configuration. You can change this to can0 or whatever other interface you wish to use.
