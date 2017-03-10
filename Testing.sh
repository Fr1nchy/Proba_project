#!/bin/bash

echo "Mise en place des tests differents !"
echo "Attention, programme en python non optimise, cela peut prendre beaucoup de temps"

echo "Test 300"

head -300 BaseReuters-29 > Test_300
time python3 projetfinal.py Test_300

echo "Test 1000"

head -1000 BaseReuters-29 > Test_1000
time python3 projetfinal.py Test_1000

echo "Test Jeu Complet"

time python3 projetfinal.py BaseReuters-29


