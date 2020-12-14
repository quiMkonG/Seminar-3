# Seminar-3
Seminar 3 SCAV. UPF.

# Quim Marcé - 205523. UPF.

Exercise 1)

Files: ex1.py

This file is aimed to be run from terminal with the sequence: python3 ex1.py x y

Where x is the input file we want to operate with and y is the height size at which we want it to be scaled. After that, the file executes 4 commands with subprocesses that scale the video and afterwards they convert it to the corresponding video codec. The av1 converted is extracted from Source 1.

Source 1: https://trac.ffmpeg.org/wiki/Encode/AV1


Exercise 2)

This file is aimed to be run from terminal using the following sequence: python3 ex2.py file1 file2 file3 file4

It basically maps all the video inputs into a 1 output file. I have not put them into one single screen because I could not find a way to do it without changing all the video codecs to only 1, therefore, the different videos are in different tracks, which can be watched in VLC by going to "video->tracks".


Exercise 3)

This file is aimed to be run from terminal with the sequence: python3 ex3.py filename

The ffmpeg tools used in the sequence can be found in the following link.

https://ffmpeg.org/ffmpeg.html

Exercise 4)

In order to turn on the stream we can just compile exercise 3 script. To turn it off is enough with pressing "q" in the terminal to kill the process.

I'm sorry this seminar is not as elaborate as the others but I just had to invest more time in studying for final exams :_____)
