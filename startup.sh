#!/bin/sh

echo "Run id"
/usr/bin/id
echo "RAN id"

cd /home/w2cxm/Documents
. venv/bin/activate
bash ./transmit.sh
