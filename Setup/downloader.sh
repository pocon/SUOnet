#!/bin/bash

for c in {101..102}
do
    html2pdf http://localhost:8000/d/ambush/$c/ /home/patrick/Desktop/Ambush1/Ambush_$c.pdf
    (( c++ ))
done

echo "Finished Downloading Checkpoints"
