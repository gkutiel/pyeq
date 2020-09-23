#!/usr/local/bin/fish
python main.py
latexmk -xelatex main.tex
lp main.pdf
