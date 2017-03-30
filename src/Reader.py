#!/usr/bin/python
# -*- mode: python; coding: utf-8 -*-

# Copyright (C) 2014, Oscar Acena <oscaracena@gmail.com>
# This software is under the terms of GPLv3 or later.

from __future__ import print_function

import sys
from bluetooth.ble import GATTRequester


class Reader(object):
    def __init__(self, address):
        self.requester = GATTRequester(address, False)
        #self.connect()
        #self.request_data()

    def connect(self):
        print("Connecting...", end=' ')
        sys.stdout.flush()

        self.requester.connect(True, 'random')
        print("OK!")

    def requestName(self):
        data = self.requester.read_by_uuid(
                "00002a00-0000-1000-8000-00805f9b34fb")[0]
        try:
            print("Device name: " + data.decode("utf-8"))
        except AttributeError:
            print("Device name: " + data)

    def request_data(self, handle=0x01, index=0):
        data = self.requester.read_by_handle(handle)[index]

        print("bytes received:", end=' ')
        for b in data:
            print(hex(ord(b)), end=' ')
        print("")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <addr>".format(sys.argv[0]))
        # C5:90:D7:25:09:80
        sys.exit(1)

    reader = Reader(sys.argv[1])
    # reader = Reader.Reader("C5:90:D7:25:09:80")
    reader.connect()
    reader.requestName()
    print("Done.")
