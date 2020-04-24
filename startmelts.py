# -*- coding: utf-8 -*-
import subprocess as sub
import pyautogui as pgui

sub.run('./Melts-rhyolite-public')

pgui.click(50,50)
pgui.typewrite(['y', 'enter', 'n', 'enter', 'y', 'enter'])