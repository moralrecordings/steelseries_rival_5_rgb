Lighting fix for the SteelSeries Rival 5
========================================

If you (like me) were unlucky enough to buy a SteelSeries Rival 5 and didn't know it required a 1GB Windows Electron app running in the background to turn off the default blinding colour-cycling rainbow, here's a Python script to send a single RGB update to the mouse. 

The only requirements are Python 3 and pyusb. This has only tested on Linux; Windows and macOS may need further work.

Instructions
============

Install Python 3 and pyusb (if you haven't already). You can either run ./steelseries.py as root, or copy it and 49-steelseries.rules to /etc/udev/rules.d/ so that it runs every time you plug the mouse in.
