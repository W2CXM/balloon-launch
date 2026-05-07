
rpicam-still --width 320 --height 256 -o latest_raw.jpg

python3 telemetry.py

pysstv --mode MartinM1 latest_pro.jpg sstv.wav

python3 serialout.py

mv latest_raw.jpg "dump/raw_$(date +%H%M).jpg"
mv latest_pro.jpg "dump/pro_$(date +%H%M).jpg"

