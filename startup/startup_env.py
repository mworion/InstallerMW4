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
import sys
import pathlib
import venv
import platform
from startup_logging import log
from startup_helper import prt, run, version


def findfile(startDir, pattern):
    """ """
    for root, dirs, files in os.walk(startDir):
        for name in files:
            if name.find(pattern) >= 0:
                return root + os.sep + name

    return None


class Envbuilder(venv.EnvBuilder):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        self.context = None
        super().__init__(*args, **kwargs)

    def post_setup(self, context):
        """ """
        self.context = context
        binPath = os.path.dirname(findfile(os.getcwd(), "activate")) + os.pathsep
        os.environ["PATH"] = binPath + os.environ["PATH"]


def run_python_in_venv(venv_context, command) -> bool:
    """ """
    command = [venv_context.env_exe] + command
    return run(command)


def run_bin_in_venv(venv_context, command) -> bool:
    """ """
    command[0] = str(pathlib.Path(venv_context.bin_path).joinpath(command[0]))
    return run(command)


def get_os_version() -> str:
    """ """
    if platform.system() == "Darwin":
        return platform.platform(terse=True)
    elif platform.system() == "Windows":
        return platform.win32_ver()[1]
    elif platform.system() == "Linux":
        return platform.release()
    else:
        return "unknown"


def venv_create(venv_path, upgrade=False) -> Envbuilder:
    """ """
    prt("-" * 45)
    prt("MountWizzard4")
    prt("-" * 45)
    prt(f"script version   : {version}")
    prt(f"platform         : {platform.system()}")
    prt(f"machine          : {platform.machine()}")
    prt(f"python           : {platform.python_version()}")
    prt("-" * 45)

    if upgrade:
        prt("Update virtual environment")
        Envbuilder(with_pip=True, upgrade=upgrade)

    existInstall = os.path.isdir("venv")
    if existInstall:
        prt("Activate virtual environment")
    else:
        prt("Install and activate virtual environment")

    venv_builder = Envbuilder(with_pip=True)
    venv_builder.create(venv_path)

    log.info("-" * 100)
    log.info(f"script version   : {version}")
    log.info(f"os platform      : {platform.system()}")
    log.info(f"os version       : {get_os_version()}")
    log.info(f"sys.executable   : {sys.executable}")
    log.info(f"actual workdir   : {os.getcwd()}")
    log.info(f"machine          : {platform.machine()}")
    log.info(f"cpu              : {platform.processor()}")
    log.info(f"python           : {platform.python_version()}")
    log.info(f"python runtime   : {platform.architecture()[0]}")
    log.info(f"upgrade venv     : {upgrade}")
    log.info("-" * 100)

    return venv_builder.context
