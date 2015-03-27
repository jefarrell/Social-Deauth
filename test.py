# Testing a python version of Julian Oliver's "Social Deauth" script
# http://julianoliver.com/output/log_2013-02-12_16-55
# Designed to run on a Raspberry Pi
# Requires arp-scan and aireplay-ng

import subprocess
import os


def testing():
    try:
            #make_mon = subprocess.call(['sudo','airmon-ng','start','mon0','11'])
            scan = subprocess.check_output(['sudo','arp-scan','--localnet','--interface=en1'])
            tscan = scan.split("\t")
           # print tscan[1::2]
            #print type(tscan[1:2])
            targets = tscan[1::2]
            print targets
    except Exception, e:
            print "Error:", e





testing()

