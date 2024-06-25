# fivedollarwrench
The $5 wrench solution to heavy trucks CAN hacking

![](https://imgs.xkcd.com/comics/security.png)

Easy solutions for messy problems.

# Research
* [Automated Threat Evaluation of Automotive Diagnostic Protocols](https://www.researchgate.net/publication/351483528_Automated_Threat_Evaluation_of_Automotive_Diagnostic_Protocols) 

# CAN Tools

## Tool: PythonCAN
[Python CAN](./pythoncan)
## Tool: Caring Caribou

**Link:**
https://github.com/CaringCaribou/caringcaribou

Using Caring Caribou to discover UDS devices on the CAN network.
```
caringcaribou -i <INTERFACE> uds discovery -min 0x18daf100 -max 0x18daf1ff

# INTERFACE could be something like vcan0 or can0, etc.
```

To do an automated UDS discovery you can try something like
```
caringcaribou -i <INTERFACE> uds auto -min 0x18daf100 -max 0x18daf1ff
```
Full docs:
https://github.com/CaringCaribou/caringcaribou/blob/master/documentation/uds.md


## Tool: CANCat

## Tool: Scapy

* [Video: Automotive Pentesting with Scapy](https://www.youtube.com/watch?v=7D7uNqPWrXw)

## Tool: TruckDevil


## Tool: SavvyCAN

## Additional Resources

* [Awesome CANbus](https://github.com/iDoka/awesome-canbus)

# Reverse Engineering

* [RE Tooling](https://github.com/wtsxDev/reverse-engineering)
* [Godbolt](https://godbolt.org/) - Compare compilers output online
* [Dogbolt](https://dogbolt.org/) - Compare decompilers online
