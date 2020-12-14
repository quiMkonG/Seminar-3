import subprocess as sp
import sys

source = sys.argv[1]
size = sys.argv[2]

if size == "720":
    w = 1280
    h = 720

elif size == "480":
    w = 640
    h = 480

elif size == "240":
    w = 360
    h = 240

elif size == "120":
    w = 160
    h = 128

else:
    print("Please introduce a valid value for the resize operation (720, 480, 240, 120)")

command_vp8 = "ffmpeg -i {} -vf scale={}:{} -c:v vp8 {}_{}_vp8.webm".format(source,w,h,source[:-4],w)
command_vp9 = "ffmpeg -i {} -vf scale={}:{} -c:v vp9 {}_{}_vp9.webm".format(source,w,h,source[:-4],w)
command_h265 = "ffmpeg -i {} -vf scale={}:{} -c:v libx265 {}_{}_h265.mp4".format(source,w,h,source[:-4],w)
command_av1 = "ffmpeg -i {} -vf scale={}:{} -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental {}_{}_av1.mkv".format(source,w,h,source[:-4],w)

sp.run(command_vp8, shell = True)
sp.run(command_vp9, shell = True)
sp.run(command_h265, shell = True)
sp.run(command_av1, shell = True)
