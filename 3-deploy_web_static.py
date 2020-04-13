#!/usr/bin/python3
# Fabric script to generate .tgz archive file

from fabric.api import *
from time import strftime as ti
import os

env.user = 'ubuntu'
env.hosts = ['34.74.199.48', '52.72.131.38']


def do_pack():
    """Fabric script to compress files in web_static"""
    local("mkdir -p versions")
    ver = ti("%Y%m%d%H%M%S")
    arc = local("tar -cvzf versions/web_static_{}.tgz web_static".format(ver))

    if arc.failed:
        return False
    else:
        return ("versions/web_static_{}.tgz".format(ver))


def do_deploy(archive_path):
    """Fabric script to deploy web_static to servers"""
    if os.path.exists(archive_path):
        new_path = archive_path[9:]
        de_path = '/data/web_static/releases/{}/'.format(new_path)[0:-4]
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(de_path))
        run('tar -xzf /tmp/{} -C {}'.format(new_path, de_path))
        run('rm /tmp/{}'.format(new_path))
        run('mv  {}/web_static/* {}'.format(de_path, de_path))
        run('rm -rf {}/web_static'.format(de_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(de_path))
        print('New version deployed successfully!')
        return True
    return False


def deploy():
    """Created and distributes an archinve to two web servers"""
    archive_path = do_pack()
    if archive_path is False:
        return False
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
