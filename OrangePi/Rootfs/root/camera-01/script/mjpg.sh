#!/bin/bash

# Run after system boot
mjpg_streamer -i "input_file.so -d 0 -f /root/camera-01/ -n opencv.jpg" -o "output_http.so -p 8080"
