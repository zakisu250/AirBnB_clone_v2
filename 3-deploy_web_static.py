#!/usr/bin/python3
""" Fabric script that creates and distributes an archive to your web servers, using the function deploy: """

from fabric.api import env, put, run, local
from os.path import exists
import time

env.hosts = ['54.174.136.120', '34.207.188.128']

def do_pack():
    """ Packing the directory to create .tgz file """
    stime = time.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static/".format(stime))
    return ("versions/web_static_{}.tgz".format(stime))

def do_deploy(archive_path):
    """ distributes an archive to the web servers """
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

def deploy():
    """ Create and deploy the web_static archive """
    archived = do_pack()
    if not archived:
        return False
    return do_deploy(archived)
