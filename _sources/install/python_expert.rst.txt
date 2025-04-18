Install Python3 expert add-ons
==============================
This section is for users who are familiar with python and have some experience.

Updating python in your existing environment
--------------------------------------------

This is a step which should be done if you are familiar with some pc experience.
Hence the steps are not complicated, the setups of you environment might be
somehow special and need a adjusted treatment. The following steps explain a
standard procedure.


Update python version on your windows computer
-----------------------------------------------
Please go to the python website an download the appropriate python version. On
windows please check the selection of the 32bit or 64bit correctly. It should be
the version you have already chosen.

Start the python installer. If everything went right, it will show an update
offer. If so, please chose that and you get the upgrade. If you would like to
switch from 32bit to 64bit or vice versa, the updater only shows a new install.
In this case please deinstall the old version manually. Than it's like a new
python3 installation, please see above.

Having your python version updated on you computer, you have to update the new
version to you work environment(s), too. There are two ways to do that. First you
could use the install script provided and install MW in a new work dir. You could
copy all you settings (except the 'venv' folder) to the new workdir. Another way
is to open a command window, change to your work directory and run the command:

.. code-block:: python

    python -m venv --upgrade venv

This will upgrade your work environment to the python version of your computer
(so the updated one)

.. note::
    Before doing any changes or updates, please do a backup of your environment
    to be safe in case of errors in the update process. This could simply be
    done by making a copy of your work folder.
