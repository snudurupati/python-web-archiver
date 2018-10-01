#!/bin/bash
mv tftd ./tftd_$(date +%m%Y)
mkdir ./tftd
cp ./template/* ./tftd
python ./monthly.py

