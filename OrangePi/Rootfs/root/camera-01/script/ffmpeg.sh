#!/bin/bash

# Run after system boot
# 192.168.8.5 is wifi camera's ip
ffmpeg -rtsp_transport tcp -i "rtsp://192.168.8.5:554/user=admin&password=&channel=1&stream=0.sdp" -vf fps=1/2 -update 1 "/root/camera-01/update-capture.jpg" -f segment -vcodec copy -an -copytb 1 -reset_timestamps 1 -segment_time 300 -segment_format avi -strftime 1 "/root/camera-01/storage/capture-%Y-%m-%d_%H-%M-%S.avi" -f flv -vcodec copy -an "rtmp://127.0.0.1:1935/live/camera-01" -y
