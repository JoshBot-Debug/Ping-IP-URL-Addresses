# mStatus.py
This repo can be used to ping IP and URL addresses's constantly in timed intervals. It will send and email notification if any of the IP or URL addresses's are not reachable.
The program is stripped down to make it easier to implement it in other programs if you want to do that.

# System Requirments
- Windows 7 or greater
- Linux (tested on CentOs)
- Has not been tested on Mac

# How to use
Once you've cloned the repo on your computer, install all the required packages using the requirments.txt file. If you have pip installed use "pip install -r requirements.txt".
To run the app just call "main.py" from command prompt and pass the path of the "config.yaml" file like this : "python main.py C:\path\to\file\config.yaml"

# config.yaml
The program requires that you pass a "config.yaml" file when running. Check out the example file in the repo
