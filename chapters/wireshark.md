## 🛠️ **Tutorial: Using Wireshark for J1939 Analysis in Linux**

### 📋 **What You’ll Need**

* Linux system with CAN interface (`can0`, `vcan0`, or USB-to-CAN device)
* `Wireshark` installed
* `can-utils` for setup
* Kernel ≥ 5.4 recommended (for `J1939` protocol support)
* Root or sudo access

---

## 1. ✅ **Set Up Your CAN Interface**

### Option A: **Use a Virtual CAN Interface**

This is great for testing.

```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

### Option B: **Physical CAN Interface (e.g., USB CAN device)**

Check your CAN device:

```bash
ip link
```

Bring it up (example for `can0` at 250kbps, common in J1939):

```bash
sudo ip link set can0 type can bitrate 250000
sudo ip link set up can0
```

---

## 2. 🧪 **Install Wireshark and can-utils**

```bash
sudo add-apt-repository ppa:wireshark-dev/stable -y
sudo apt install wireshark can-utils
```

You may need to add your user to the `wireshark` group:

```bash
sudo usermod -aG wireshark $USER
newgrp wireshark
```

---

## 3. 🧬 **Enable J1939 Protocol Decoding in Wireshark**

Wireshark supports J1939 natively as of recent versions.

1. Launch Wireshark:

   ```bash
   sudo wireshark &
   ```

2. In the **Capture Interface** window, select your CAN interface (`can0`, `vcan0`).

3. Under `Edit` → `Preferences`:

   * Go to `Protocols` → `J1939`.
   * Enable options like “Reassemble fragmented messages” or “Decode PGNs.”

---

## 4. 🎯 **Capture J1939 Traffic**

Start a capture on your CAN interface.

```bash
sudo wireshark -k -i can0
```

Wireshark will begin to display CAN frames. If J1939 traffic is present, it will be decoded based on PGNs (Parameter Group Numbers).

---

## 5. 🔍 **Use Display Filters**

Here are **useful J1939 filters**:

| Filter                              | Description                         |
| ----------------------------------- | ----------------------------------- |
| `j1939`                             | Shows only J1939 packets            |
| `can.protocol == 6`                 | J1939 protocol ID                   |
| `j1939.pgn == 65226`                | Filter for specific PGN (e.g., DM1) |
| `j1939.source_address == 0x00`      | Filter by source address (ECU)      |
| `j1939.destination_address == 0xFF` | Broadcast messages                  |
| `j1939.priority == 3`               | Show messages with priority 3       |

To show all PGNs (diagnostics, emissions, etc.), use:

```plaintext
j1939
```

---

## 6. 📖 **Interpret J1939 Data**

* **PGN (Parameter Group Number)**: Identifies the message type (e.g., 65226 = DM1).
* **SA (Source Address)**: The ID of the sender ECU.
* **DA (Destination Address)**: Receiver ECU; `0xFF` means broadcast.
* **Data**: Raw payload that varies by PGN; can be decoded via spec or `.dbc` files.

---

## 7. 🧰 **Optional: Use `candump` to Generate J1939 Traffic**

Example:

```bash
candump vcan0
```

Or send a frame:

```bash
cansend vcan0 18FEF100#1122334455667788
```

This frame:

* PGN = 0xFEF1 (65265)
* Priority = 6
* Source Address = 0
* Data = `11 22 33 44 55 66 77 88`

---

## 8. 💡 Tips

* You can **save a capture** and open it later:

  * File → Save As → `.pcapng`
* For better dissection, consider adding a **.dbc file** or using tools like **CANvas**, **SavvyCAN**, or **kayak** if Wireshark doesn’t parse the payload to your liking.
* If you want to **log traffic** from command line:

  ```bash
  candump -L can0 > j1939_log.txt
  ```

---

## 🧩 **Troubleshooting**

* **No packets?** Check `ifconfig` or `ip link` to ensure the interface is up.
* **Not seeing PGNs?** Make sure the frames are **29-bit extended** CAN (J1939 only uses extended frames).
* **Permissions error?** Use `sudo` or ensure your user is in the `wireshark` group.

---

## 📚 Reference

* SAE J1939 Specification
* Wireshark J1939 Wiki: [https://wiki.wireshark.org/J1939](https://wiki.wireshark.org/J1939)
* Kernel J1939 SocketCAN: [https://docs.kernel.org/networking/j1939.html](https://docs.kernel.org/networking/j1939.html)

