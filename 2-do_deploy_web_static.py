#!usr/bin/python3
""" Transfer and execute archives to servers """
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo

env.hosts = ['54.174.136.120', '34.207.188.128']


def do_deploy(archive_path):
    """ Deploy the archive in the argument """
    if (os.path.isFile(archive_path) is Flase):
        return False
    try:
        new_file = archive_path.split('/')[-1]
        file_name = ("/data/web_static/releases/" + new_file.split('.')[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(file_name))
        run("sudo tar -xzf /tmp/{} -C {}".format(new_file, file_name))
        run("sudo rm /tmp/{}".format(new_file))
        run("sudo mv {}/web_static/* {}/".format(new, new))
        run("sudo rm -fr {}/web_static".format(new))
        run("sudo rm -fr /data/web_static/current")
        run("sudo ln -s {} /data/web_static/surrent".format(new))
        return True
    except:
        return False
