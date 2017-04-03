from __future__ import print_function
from bluepy.btle import Peripheral, Scanner, DefaultDelegate, Debugging
from ScanDelegate import ScanDelegate

class RoombaOverBle(Peripheral):
    """ Derived class from Peripheral class. This handles connection for Roomba device """

    DebugLevel = 0
    _ScanTimeout = 10.0

    def __init__(self, DebugLevel=0, ScanTimeout=3.0):
        """ Constructor """
        Peripheral.__init__(self)
        self.DebugLevel = DebugLevel
        self._ScanTimeout = ScanTimeout
        self.txToRoombaCharacteristic = None
        self.rxFromRoombaCharacteristic = None

        Debugging = DebugLevel != 0     # global variable in bluepy.btle

    def _connectWithDevice(self, deviceName):
        """ establish BLE connection with device which has string deviceName for Short Name Descriptor """
        scanner = Scanner().withDelegate(ScanDelegate())
        devices = scanner.scan(self._ScanTimeout)
        deviceScanEntry = None          # creating variable
    
        for dev in devices:
            if (self.DebugLevel >= 1):
                print ("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
            for (adtype, desc, value) in dev.getScanData():
                if (self.DebugLevel >= 2):
                    print (adtype, end='')
                    #print (adtype)
                if (self.DebugLevel >= 1):
                    print ("  %s = %s" % (desc, value))
                if (adtype == 8) and (value == "Roomba"):
                    deviceScanEntry = dev
        try:
            if (deviceScanEntry == None):
                # throw error
                raise RuntimeWarning("Device with name %s not found" % (deviceName))
        except RuntimeWarning:
            print (RuntimeWarning.args)
            raise
        else:
            self.connect(deviceScanEntry)

    def connectWithRoomba(self):
        """ establish BLE connection Roomba device. Assumes Roombas has deviceName == Roomba """
        self._connectWithDevice ("Roomba")

    def dumpBleTable(self):
        """ Debug function... simply dumps entire contents of the remote BLE device """
        roombaServices = self.getServices()
        print (roombaServices)
        for currentService in roombaServices:
            print (currentService)
    
        roombaCharacteristics = self.getCharacteristics()
        print (roombaCharacteristics)
        for currentCharacteristics in roombaCharacteristics:
            print (currentCharacteristics)
    
        roombaDescriptors = self.getDescriptors()
        print (roombaDescriptors)
        for currentDescriptors in roombaDescriptors:
            print (currentDescriptors)

    def _findCharacteristic(self, characteristicsID):
        """ Parse all characteristics and locate the one with the given UUID """
        roombaCharacteristics = self.getCharacteristics()
        if (self.DebugLevel >= 3):
            print (roombaCharacteristics)
        for currentCharacteristics in roombaCharacteristics:
            if (self.DebugLevel >= 2):
                print (currentCharacteristics.getHandle(), currentCharacteristics)
            if (currentCharacteristics.uuid == characteristicsID):
                if (self.DebugLevel >= 2):
                    print ("found", currentCharacteristics)
                return currentCharacteristics

        return None

    def findTxCharacteristic(self):
        """ Find characteristic which has UUID 6e400002-b5a3-f393-e0a9-e50e24dcca9e """
        self.txToRoombaCharacteristic = self._findCharacteristic("6e400002-b5a3-f393-e0a9-e50e24dcca9e")

    def findRxCharacteristic(self):
        """ Find characteristic which has UUID 6e400003-b5a3-f393-e0a9-e50e24dcca9e """
        self.rxFromRoombaCharacteristic = self._findCharacteristic("6e400003-b5a3-f393-e0a9-e50e24dcca9e")

if __name__ == '__main__':

    roombaOverBle = RoombaOverBle(DebugLevel=99)
    roombaOverBle.connectWithRoomba()
    #roombaOverBle.dumpBleTable()
    roombaOverBle.findTxCharacteristic()
    roombaOverBle.findRxCharacteristic()
    print (roombaOverBle.txToRoombaCharacteristic.supportsRead() )
    print (roombaOverBle.txToRoombaCharacteristic.propertiesToString() )
    print (roombaOverBle.rxFromRoombaCharacteristic.supportsRead() )
    print (roombaOverBle.rxFromRoombaCharacteristic.propertiesToString() )
    roombaOverBle.txToRoombaCharacteristic.write("c")

