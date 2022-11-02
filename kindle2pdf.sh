echo "não funcional"
exit 1

scrcpy --crop 720:1048:0:256 -nN -r oi.mkv --record-format mkv
mplayer -vf screenshot oi.mkv
img2pdf -o teste.pdf shot00*
#
# https://stackoverflow.com/a/8483797
adb shell input keyevent 22
# https://stackoverflow.com/a/27774325
adb shell screencap -p | sed 's|\r$||' > screenshot.png
