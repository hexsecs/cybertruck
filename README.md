# fivedollarwrench
The $5 wrench solution to heavy trucks CAN hacking

![](https://imgs.xkcd.com/comics/security.png)

Easy solutions for messy problems.

# Discovery

## Tool: Caring Caribou

Using Caring Caribou to discover UDS devices on the CAN network.
```
caringcaribou -i <INTERFACE> uds discovery -min 0x18daf100 -max 0x18daf1ff
```

To do an automated UDS discovery you can try something like
```
caringcaribou -i <INTERFACE> uds auto -min 0x18daf100 -max 0x18daf1ff
```
Full docs:
https://github.com/CaringCaribou/caringcaribou/blob/master/documentation/uds.md
