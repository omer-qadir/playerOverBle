# playerOverBle
Interface layer to translate player server (ref player/stage) from TCP to BLE

# Run RTT client to observe debug printfs from Devkit

https://devzone.nordicsemi.com/question/83524/how-to-use-rtt-viewer-or-similar-on-gnulinux/
https://devzone.nordicsemi.com/question/44790/rtt-on-os-x/

1) In a shell type "JLinkExe -device nrf52 -if swd -speed 4000"
2) type "connect"

3) in another shell run "JLinkRTTClient"
This shell will display debugs

# Setup Makefile based compilation in Ubuntu

https://devzone.nordicsemi.com/tutorials/7/

(Don't need this -- will use Virtual box and windows client)

# Devkit related tips


while debugging without roomba, connect pin 28 to VDD or 5V
When the devkit is in normal state upon boot-up
* LED 5 appears constantly lit (although it is flickering very fast)
* LED 1 is blinking when waiting for connection
* LED 1 becomes constantly lit if a connection is established
* the cortex goes to sleep after a certain time of not receiving any connections and then LED 1 is off. hit reset.

# PyBlueZ: Python BLE related


PyBlueZ python scripts use gattlib which doesn't seem to have very good documentation.
Reading https://github.com/matthewelse/pygattlib/blob/master/src/gattlib.cpp to decode what the various arguments mean for each function
some rudimentary documentation here:
https://bitbucket.org/OscarAcena/pygattlib/overview

# bluePy: Python BLE related


bluez python library documentation here
https://github.com/IanHarvey/bluepy/blob/master/docs/


## gitWorkspace/pybluez/examples/advanced

this folder contains basic bluetooth code (not BLE code)

## gitWorkspace/pybluez/examples/ble

this folder contains BLE related example code. This code is slightly modified from source
 * read_name.py: requester.connect() is given optional argument 'random' (random channel rather than public channel) otherwise connection request fails with devkit
 * scan.py: discover takes timeout value in seconds. This is increased otherwise it reads too few

The scan.py needs to be executed as root.

## gitWorkspace/pygattlib/examples

this folder contains BLE related example code. Better than pybluez/examples/ble. It will also need the same modifications as for pybluez (above).
