#!/bin/bash

mosquitto_sub -u agiot -P 2019 -t "dev/test" > data.txt & 

mosquitto_sub -h test.mosquitto.org -t "smartfarm" > actuator.txt
