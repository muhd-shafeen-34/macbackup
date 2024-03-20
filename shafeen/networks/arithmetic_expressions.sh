#!/bin/bash
echo "Enter two numbers"
read a
read b
sum=`expr $a + $b`
diff=`expr $a - $b`
mult=`expr $a \* $b`
div=`expr $a / $b`
mod=`expr $a % $b`
echo "$a+$b=$sum"
echo "$a-$b=$diff"
echo "$ax$b=$mult"
echo "$a/$b=$div"
echo "$a%$b=$mod"

