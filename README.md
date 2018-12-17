# Astrophysics Project

## ezweb.py

ezweb.py is a library for parsing output data from Richard Townsend's [EZ-Web](http://www.astro.wisc.edu/~townsend/static.php?ref=ez-web). EZ-Web is a stellar evolution simulator that outputs a ton of information about the lifecycle of a star.

## final.py

final.py uses the ezweb.py library and matplotlib to make graphs from ezweb_02526 (a 0.8 M☉ star).

The functions implemented per step are:

* Opacity vs log(R)
* Adiabatic and Radiative temperature gradiant vs log(T)
* Material distribution vs log(R)

The functions implemented across the whole project are:

* HR Diagram (with the main sequence outlined)
* Power generation vs time
