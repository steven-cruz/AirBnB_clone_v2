#!/usr/bin/python3
# distributes an archive to your web servers, using the function do_deploy.

from fabric.api import *
import os

env.user = "ubuntu"
env.hosts = ['34.74.199.48', '52.72.131.38']


def do_deploy(archive_path):
    """ Fabric script to deply web_static to servers """
    if os.path.exists(archive_path):
        new_path = archive_path[9:]
        de_path = '/data/web_static/releases/{}/'.format(new_path)[0:-5]
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
