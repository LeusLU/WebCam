#!/bin/bash

# Run after system boot
# connect to wifi
wpa_supplicant -i wlan3 -c /etc/network/wpa_supplication.conf &
dhcpcd wlan3 &
