# fivedollarwrench
The $5 wrench solution to heavy trucks CAN hacking

![](https://imgs.xkcd.com/comics/security.png)

Dirty solutions for messy problems.

## Discovery

## Technique #1
Using Caring Caribou to discover UDS devices on the CAN network.
```
caringcaribou -i <INTERFACE> uds discovery -min 0x18daf100
```
