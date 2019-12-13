#!/bin/bash
rpi-lora-tranceiver-master/dragino_lora_app/mqtt_sub.sh 

while true; do
	rpi-lora-tranceiver-master/dragino_lora_app/dragino_lora_app sender
	sleep 20
done
