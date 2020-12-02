# ################# Start the server and listen for connections ########################################################

import sockets
import sys
import os
ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    thePort = int(os.environ.get('PORT', 8080))  # Default port 8080
else:
    thePort = 8080

if __name__ == '__main__':  # file is executed
    if len(sys.argv) < 2:
        sys.argv.append(str(thePort))  # Port 8080 default port
    if len(sys.argv) < 3:
        sys.argv.append(str(20))  # 20 moves default maximal return length of maneuver
    if len(sys.argv) < 4:
        sys.argv.append(str(3))  # 3 second default timeout for search
    print('startserver')
    sockets.server_start(sys.argv)
else:
    def start(port, maxmoves, timeout):
        sockets.server_start((-1, port, maxmoves, timeout))
