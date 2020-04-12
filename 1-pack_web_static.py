#!/usr/bin/python3
# Fabric script to generate .tgz archive file

from fabric.api import *
from time import strftime as ti


def do_pack():
    """Fabric script to compress files in web_static"""
    local("mkdir -p versions")
    ver = ti("%Y%m%d%H%M%S")
    arc = local("tar -cvzf versions/web_static_{}.tgz web_static".format(ver))

    if arc is None:
        return None
    else:
        return ("versions/web_static_{}".format(ver))
