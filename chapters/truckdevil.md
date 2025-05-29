### TruckDevil Documentation

**Overview**
TruckDevil is a framework designed for interacting with and assessing ECUs that use J1939 for communication on the CANBUS.

**Requirements**
- **Hardware:** Supports Macchina M2 as well as any python-can device (e.g., SocketCAN).
- **Software:** Requires Python 3. Additional software for flashing M2 firmware.

**Installation**
1. Clone the repository:
    ```sh
    git clone https://github.com/LittleBlondeDevil/TruckDevil.git
    ```
2. If using M2:
   - Install Arduino Desktop IDE, Macchina M2 Board Configuration, and drivers.
   - Include `due_can` and `can_common` libraries in the IDE.
   - Upload `m2_sketch.ino` to the M2.

**Usage**
1. **Interactive Mode:**
    ```sh
    python truckdevil.py
    ```
    Use commands like `add_device`, `list_device`, `list_modules`, and `run_module`.

2. **Command Line:**
    ```sh
    python .\truckdevil.py add_device m2 can0 250000 COM5 run_module read_messages set num_messages 5 print_messages
    ```

**Creating Custom Modules**
- Add Python files in the `modules` folder with the function:
    ```python
    def main_mod(argv, device)
    ```
  There is a template module provided to get started with.

**J1939 API**
- Refer to `j1939.py` for documentation and examples.

For more detailed information, visit the [TruckDevil GitHub repository](https://github.com/LittleBlondeDevil/TruckDevil).
