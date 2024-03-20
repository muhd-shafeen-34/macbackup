#!/bin/bash
N=10
a=0
b=1
sum=0 
echo "The Fibonacci series is : "
for (( i=0; i<=N; i++ ))
do
    echo  "$a "
    sum=`expr $sum + $a`
    fn=$((a + b))
    a=$b
    b=$fn
done
echo -e "\nthe sum of fibonacci series $sum"

