import subprocess as sp
import sys

source = sys.argv[1]

command = "ffmpeg -re -i {} -an -c:v copy -f mpegts udp://@224.2.2.2:2222".format(source)

sp.run(command, shell = True)
