#!/bin/bash

# When actually executing, remove the e to remove failing on error
set -ve

source /home/w2cxm/Documents/venv/bin/activate

while true; do
	(rpicam-jpeg --output "output.jpg" --raw --nopreview --timeout 0.01 --width 512 --height 512;
	 stats="W2CXM time=$"
	 magick output.jpg -background Black -fill White label:'W2CXM' +swap -gravity Center -append anno.jpg;
	 pysstv --vox --mode MartinM1 "anno.jpg" sstv.wav) &
	# We need vox enabled on the transmitting baofeng!
	aplay -D plughw:2,0 sstv.wav
done
