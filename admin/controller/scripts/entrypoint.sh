#!/bin/bash

# Setting nameserver for DNS resolution
echo "nameserver 8.8.8.8" >> /etc/resolv.conf

# Infinite loop to keep the script running
while true; do

  # Running actions-controller script in python3
  python3 /var/task/actions-controller.py 

  # Sleeping for 305 seconds before next iteration
  sleep 305
done
