# nhl-schedule

![Brief showcase of the scoreboard](https://github.com/rlynch7321/nhl-schedule/blob/master/showcase.gif)

This repository contains some source code for a Python program that access the NHL's official API to retrieve scores and render them onto an LED matrix.

When the program is first run, it gets the current day's schedule and displays each game for 5 seconds.

When displaying a game, there are three cases:
1. The game has not started
 - If the game hasn't started yet, the program will display the teams scheduled to play and the start time in EST.
2. The game is in progress
 - The program will display the teams playing, their scores, the period, and the amount of time remaining in the period (or, if applicable, which intermission is in progress)
3. The game is over
 - The program will display the teams that played and their final scores, as well as an indication of whether the game went to overtime or a shootout (FINAL, FINAL OT, or FINAL SO)


This code was not prepared for plug-and-play use. It is only intended to share the source code that runs my LED board. The project is very much a work in progress.

This project was my second ever Python project and one of the deepest dives into python that I've taken. My first experiment was a simple Reddit bot that could perform actions on the website via the command line. I have no classroom Python experience but I've really come to enjoy teaching myself the language.
