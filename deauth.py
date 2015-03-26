
import subprocess
import os
MACs = []

def testing():
    try:
            make_mon = subprocess.call(['sudo','airmon-ng','start','mon0','11'])
            scan = subprocess.check_output(['sudo','arp-scan','--localnet','--interface=mon0'])
            nscan = scan.split("\t")
            print nscan[1::2]
    except Exception, e:
            print "Error:", e





testing()

