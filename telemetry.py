#import Adafruit_DHT as dht
#import serial
import time
from PIL import Image, ImageDraw, ImageFont

#Set DATA pin
#DHT = 2
#while True:
    #Read Temp and Hum from DHT22
 #   h,t = dht.read_retry(dht.DHT11, DHT)
    #Print Temperature and Humidity on Shell window
  #  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t,h))
   # sleep(1) #Wait 5 seconds and read again

#load and mod image
try:
    img = Image.open('latest_raw.jpg').convert('RGB')
except FileNotFoundError:
    print("Error: Image file not found. Please check the path.")
    # Fallback to blank if file is missing
    img = Image.new('RGB', (320, 256), color='black')

draw = ImageDraw.Draw(img)

#callsign_box = [0, 0, 60, 256]
#draw.rectangle(callsign_box, fill="#38d4ff")

text = "W2CXM"
font_path = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
font_size = 50

try:
    font = ImageFont.truetype(font_path, font_size)
except OSError:
    print("Could not find the font at that path. Using default fallback.")
    font = ImageFont.load_default()

# Get dimensions for the text canvas
text_bbox = draw.textbbox((0, 0), text, font=font)
text_w = text_bbox[2] - text_bbox[0]
text_h = text_bbox[3] - text_bbox[1]

# Draw text on a transparent layer
txt_canvas = Image.new('RGBA', (320,256), (255, 255, 255, 0))
txt_draw = ImageDraw.Draw(txt_canvas)
txt_draw.text((0, 0), text, font=font, fill="white")

# Rotate and paste
#vertical_txt = txt_canvas.rotate(90, expand=True)
#img.paste(vertical_txt, (0, 256-text_w), vertical_txt)
img.paste(txt_canvas, (0, 0), txt_canvas)

img.save("latest_pro.jpg")

#play audio to radio
#ser = serial.Serial('/dev/ttyACM0',9600)

#ser.dtr = True
#ser.rts = False

#play audio out to serial here

#ser.dtr = False
#ser.rts = True

#ser.close()
