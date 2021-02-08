import os
from datetime import datetime

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def site(path) :

    print(path)
    if int(path[-1]) == 8:
        SITE = "kullum"
    if int(path[-1]) == 2:
        SITE = "phaterak"
    if int(path[-1]) == 3:
        SITE = "secmol"
    if int(path[-1]) == 7:
        SITE = "gangles"
    if int(path[-1]) == 1:
        SITE = "hial"
    return SITE
