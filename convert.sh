#!/bin/bash
MSCORE="/Applications/MuseScore 2.app/Contents/MacOS/mscore"
FILES=mscz/*.mscz
for f in $FILES
do
  echo "Processing $f file..."
  filename=$(basename "$f")
  extension="${filename##*.}"
  filename="${filename%.*}"
  "$MSCORE" $f -o images/examples/$filename.png -T 10 -r 72
  mv images/examples/$filename-1.png images/examples/$filename.png
  "$MSCORE" $f -o sound/examples/$filename.mp3
  "$MSCORE" $f -o sound/examples/$filename.ogg
done