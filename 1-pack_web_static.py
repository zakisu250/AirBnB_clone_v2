#!/usr/bin/python3
""" Prepare the web_static directory by packing """
from fabric.api import local
import time


#def do_pack():
#    """ Packing the directory to create .tgz file """
#    stime = time.strftime("%Y%m%d%H%M%S")
#    local("mkdir -p versions")
#    local("tar -cvzf versions/web_static_{}.tgz web_static/".format(stime))
#    return ("versions/web_static_{}.tgz".format(stime))
def do_pack():
    """
        compresses web_static files into one file
    """
    local("mkdir -p versions")
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    tar_path = "versions/web_static_{}.tgz".format(current_date)
    captured = local("tar -cvzf {} web_static".format(tar_path), capture=True)
    if captured.failed:
        return None
    return tar_path
