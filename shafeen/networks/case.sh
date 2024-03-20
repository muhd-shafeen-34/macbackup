#!/bin/bash
echo "which state you want to know"
echo "1.Kerala"
echo "2.TamilNadu"
echo "3.Karnataka"
read state
case $state in
1)echo "Trivandrum";;
2)echo "Chennai";;
3)echo "Bangalore";;
*)echo "not in list";;
esac


