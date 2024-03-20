#!/bin/bash
b=1
echo "enter a value"
read a
while [ $b -le $a ]
do
echo "value of $b = $b"
b=`expr $b + 1`
done

