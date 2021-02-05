# -*- coding: utf-8 -*-
import os
import time
import re
import pprint
import json
from flask import Flask


def get_default_iface_name_linux():
    """Method that will return our default network adapter"""

    route = "/proc/net/route"
    with open(route) as f:
        for line in f.readlines():
            try:
                iface, dest, _, flags, _, _, _, \
                    _, _, _, _, =  line.strip().split()
                if dest != '00000000' or not int(flags, 16) & 2:
                    continue
                return iface
            except:
                continue


app = Flask(__name__)
@app.route('/')
def net_interface_monitor():
    """Method that will display our network statistics"""

    device_file = '/proc/net/dev'

    # Get default network interface
    default_interface = get_default_iface_name_linux()

    with open(device_file) as f:
        for num, line in enumerate(f, 1):
            r = re.search(default_interface, line)
            if r:
                net_data = line.split()

        statistics = {
                "interface" :   net_data[0],   
                "tx"        :   {
                    "bytes"         :   int(net_data[1]),
                    "packets"       :   int(net_data[2]),
                    "errs"          :   int(net_data[3]),
                    "drop"          :   int(net_data[4]),
                    "fifo"          :   int(net_data[5]),
                    "frame"         :   int(net_data[6]),
                    "compressed"    :   int(net_data[7]),
                    "multicast"     :   int(net_data[8])
                    },
                "rx"        :   {
                    "bytes"         :   int(net_data[9]),
                    "packets"       :   int(net_data[10]),
                    "errs"          :   int(net_data[11]),
                    "drop"          :   int(net_data[12]),
                    "fifo"          :   int(net_data[13]),
                    "frame"         :   int(net_data[14]),
                    "compressed"    :   int(net_data[15]),
                    "multicast"     :   int(net_data[16])
                    }
                }

        js = json.dumps(statistics)
        return js


def main():
    if 'DURATION' in os.environ:
        # Get env var called DURATION
        duration = int(os.environ.get('DURATION'))
    else:
        # If no DURATION env var is set
        duration = 30
        print("\nMissing env variable DURATION. " +
              "We will set this duration to 30s.\n")
        print("#"*50+"\n")

    # Start API endpoint if this var is set to 'y'
    if os.environ.get('API_ENDPOINT') == 'y':
        app.run(host='0.0.0.0')
    else:
        while True:
            stats = net_interface_monitor()
            pprint.pprint(stats)
            time.sleep(duration)


if __name__ == "__main__":
    main()
