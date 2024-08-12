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
import sys
from packaging.utils import Version
from startup_logging import log
from startup_helper import prt
from startup_env import run_python_in_venv


def download_and_install_wheels(venv_context, version: Version) -> bool:
    """
    """
    preRepo = 'https://github.com/mworion/InstallerMW4'
    preSource = '/raw/main/wheels/'
    postRepo = ''
    wheels = {
        '3.0.0': {
            '3.8': [
                'PyQt5_sip-12.11.1-cp38-cp38-linux_aarch64.whl',
                'PyQt5-5.15.9-cp38.cp39.cp310-abi3-manylinux_2_17_aarch64.whl',
            ],
            '3.9': [
                'PyQt5_sip-12.11.1-cp39-cp39-linux_aarch64.whl',
                'PyQt5-5.15.9-cp38.cp39.cp310-abi3-manylinux_2_17_aarch64.whl',
            ],
            '3.10': [
                'PyQt5_sip-12.11.1-cp310-cp310-linux_aarch64.whl',
                'PyQt5-5.15.9-cp37-abi3-manylinux_2_17_aarch64.whl',
                'PyQt5-5.15.9-cp38.cp39.cp310-abi3-manylinux_2_17_aarch64.whl',
            ],
        },
    }
    log.info(f'Got version {version}')
    prt(f'Check precompiled packages for {version}')

    if version < Version('2.999'):
        log.info('No supported version')
        prt('...no supported version')
        return False

    elif Version('3.999') > version > Version('2.999'):
        versionKey = '3.0.0'
        log.info('Path version 3.x.y')

    elif Version('4.999') > version > Version('3.999'):
        log.info('Path version 4.x.y')
        prt('No precompiled packages for this version needed')
        return True

    else:
        log.info('No supported version')
        prt('...no supported version')
        return False

    ver = f'{sys.version_info[0]}.{sys.version_info[1]}'
    for item in wheels[versionKey][ver]:
        prt(f'...{item.split("-")[0]}-{item.split("-")[1]}')
        command = ['-m', 'pip', 'install', preRepo + preSource + item + postRepo]
        suc = run_python_in_venv(venv_context, command)
        if not suc:
            prt('...error install precompiled packages')
            return False
    prt('Precompiled packages ready')
    return True
