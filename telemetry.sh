#!/bin/bash

declare -i max_altitude
max_altitude=0

tail --follow /home/w2cxm/Documents/data/gps-data.json |
	(read time lat lon alt speed climb;
if (( $alt > $max_altitude )) then max_altitude=$alt; fi
echo $max_altitude)
