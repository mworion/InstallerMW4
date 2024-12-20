############################################################
# -*- coding: utf-8 -*-
#
#       #   #  #   #   #    #
#      ##  ##  #  ##  #    #
#     # # # #  # # # #    #  #
#    #  ##  #  ##  ##    ######
#   #   #   #  #   #       #
#
# Installer for MountWizzard4
#
# a Python-based Tool for interaction with the
# 10micron mounts GUI with PyQT5/6
#
# written in python3, (c) 2019-2024 by mworion
# Licence APL2.0
#
###########################################################
import os
import tarfile
import requests
from packaging.version import Version
from startup_logging import log
from startup_helper import version


def version_app_online(update_beta: bool) -> Version:
    """ """
    url = "https://pypi.python.org/pypi/mountwizzard4/json"
    try:
        response = requests.get(url).json()
    except Exception as e:
        log.error(f"Cannot determine package version: {e}")
        return Version("0.0.0")

    vPackage = list(response["releases"].keys())
    vPackage.sort(key=Version, reverse=True)
    verBeta = [x for x in vPackage if "b" in x]
    verRelease = [x for x in vPackage if "b" not in x and "a" not in x]
    log.info(f"Package Beta:   {verBeta[:10]}")
    log.info(f"Package Release:{verRelease[:10]}")

    if update_beta:
        app_version = Version(verBeta[0])
    else:
        app_version = Version(verRelease[0])

    return app_version


def version_app_local() -> Version:
    """ """
    with tarfile.open("mountwizzard4.tar.gz", "r") as f:
        for member in f.getmembers():
            if "PKG-INFO" in member.name:
                pkg = f.extractfile(member.name)
                with open("PKG_INFO", "wb") as o:
                    o.write(pkg.read())
    version_string = "0.0.0"
    with open("PKG_INFO", "r") as f:
        for line in f.readlines():
            if line.startswith("Version:"):
                version_string = line.split(":")[1]
    os.remove("PKG_INFO")
    return Version(version_string)


def get_app_version(is_test: bool, update_beta: bool, version_string: str) -> Version:
    """ """
    if version_string:
        version_app = Version(version_string)
    elif is_test:
        version_app = version_app_local()
    elif update_beta:
        version_app = version_app_online(True)
    else:
        version_app = version_app_online(False)
    return version_app


def version_script_local() -> Version:
    """ """
    return Version(version)


def version_script_online() -> Version:
    """ """
    url = "https://github.com/mworion/MountWizzard4/tree/main/support/startup.py"
    try:
        response = requests.get(url)
    except Exception as e:
        log.error(f"Cannot determine script version: {e}")
        return Version("0.0.0")

    for line in response.text.split("\n"):
        if line.startswith("version ="):
            version_string = line.split("=")[1].strip().strip("'")
            return Version(version_string)
    return Version("0.0.0")
