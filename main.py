#!/usr/bin/python3

__author__ = "Joshua Joseph Myers"
__copyright__ = "Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>"
__credits__ = ["Joshua Joseph Myers"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.1"
__maintainer__ = "Joshua Joseph Myers"
__email__ = "JoshuaMyersWebDev@gmail.com"
__status__ = "Production"

import sys
from src.mStatus import mStatus

if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except:
        file_path = input('[Config file Path]: ')

    mStatus(file_path)
