#! /bin/bash

while true; do
	mosquitto_sub -h us-west.thethings.network -t "+/devices/+/up" -u "ksw2019agiot" -P "ttn-account-v2.nJAy-JFHF3lX1Pl6iy84cGHEw_MwdIc6h-nNGsgwL8k" -v -C 1 > log.txt

	python parsing.py

	python publishMSG.py
done
