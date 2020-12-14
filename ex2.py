import subprocess as sp
import sys

source = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]]

command = "ffmpeg -i {} -i {} -i {} -i {} -c copy \
        -map 0:0 -map 0:1 \
        -map 1:0 -map 1:1\
        -map 2:0 -map 2:1\
        -map 3:0 -map 3:1\
        result.mkv".format(source[0],source[1],source[2],source[3])

sp.run(command, shell=True)
