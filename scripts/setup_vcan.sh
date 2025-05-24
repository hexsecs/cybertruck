sudo modprobe can
sudo modprobe vcan
sudo ip link set down vcan0
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
