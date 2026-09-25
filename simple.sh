#!/bin/bash

# When actually executing, remove the e to remove failing on error
set -ve

source /home/w2cxm/Documents/venv/bin/activate

while true; do
	(rpicam-jpeg --output "output.jpg" --raw --nopreview --timeout 0.01 --width 320 --height 240 --vflip;
	 stats="[W2CXM] $(tail -n 1 data/gps-data.json)"
	 magick output.jpg -background Black -fill White label:"$stats" +swap -gravity Center -append anno.jpg;
	 pysstv --vox --mode MartinM1 "anno.jpg" sstv.wav;
	 mv anno.jpg "/home/w2cxm/Documents/data/images/Image-$(date +'%H%M').jpg") &
	# We need vox enabled on the transmitting baofeng!
	cp sstv.wav sstv-playing.wav
	aplay -D plughw:2,0 sstv-playing.wav
	rm sstv-playing.wav
done
