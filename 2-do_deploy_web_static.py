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
    if os.path.isfile(archive_path) is False:
        return False
    filename = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(filename)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(filename, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(filename)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    print("New version deployed!")
    return True
