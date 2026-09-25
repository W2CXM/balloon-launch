#!/bin/bash

echo -e "time\tlat\tlon\talt"
# The gawk command was written by Claude lol
gpspipe -w -B | jq --unbuffered 'select(.class=="TPV" and .lat!=null) | "\(.time)\t\(.lat)\t\(.lon)\t\(.alt)"' -cr | gawk 'BEGIN { FS = OFS = "\t" }
{
    ts = substr($1, 1, 19)
    gsub(/[-T:]/, " ", ts)
    epoch = mktime(ts, 1)              # parse as UTC
    $1 = strftime("%H:%M:%S", epoch)   # no trailing 1 → uses TZ, DST-aware
    $2 = sprintf("%.4f", $2)
    $3 = sprintf("%.4f", $3)
    print
    fflush()
}' > /home/w2cxm/Documents/data/gps-data.json
