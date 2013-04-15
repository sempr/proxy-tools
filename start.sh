#!/bin/bash
cd `dirname $0`
python proxy-crawler.py
echo "Get Finished!"
python proxy-checker.py ip1.txt ip2.txt
echo "Check Finished!"

