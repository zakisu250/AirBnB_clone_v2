#!/usr/bin/python3
""" Prepare the web_static directory by packing """
from fabric.api import *
import time


def do_pack():
    """ Packing the directory to create .tgz file """
    stime = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz webstatic_".
              format(stime))
        return ("versions/web_static_{}.tgz".format(stime))
    except:
        return None
