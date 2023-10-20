#!/usr/bin/python3
"""
    Fabric program that executes commands to:
    - create temporary archive extraction location
    - extract archives
    - move the extracted archive to the appropriate location
    - remove temporary directories and sub-directories
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['107.23.211.94', '35.175.105.178']


def do_deploy(archive_path):
    """ distributes an archive to my web servers """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        print("New version deployed!")
        return True
    except:
        return False
