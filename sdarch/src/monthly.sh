#!/bin/bash
mv tftd /home/ananta/sdarch/src/tftd_old/tftd_$(date +%m%Y)
mkdir /home/ananta/sdarch/src/tftd
cp /home/ananta/sdarch/src/template/* /home/ananta/sdarch/src/tftd
python /home/ananta/sdarch/src/monthly.py

