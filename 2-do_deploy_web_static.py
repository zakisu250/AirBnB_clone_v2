#!/usr/bin/python3
"""
    Fabric program that executes commands to:
    - create temporary archive extraction location
    - extract archives
    - move the extracted archive to the appropriate location
    - remove temporary directories and sub-directories
"""

from fabric.api import *
import os

env.hosts = ['54.174.136.120', '34.207.188.128']


def do_deploy(archive_path):
    """ distributes an archive to my web servers """
    if exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        print("New version deployed!")        
        return True
    except:
        return False
