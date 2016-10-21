.. _installation:

Installation
============

The installation is using the Python distribution system `Anaconda`_ to maintain software dependencies.
Anaconda will be installed during the installation process in your home directory ``~/anaconda``.

The installation process setups a conda environment named ``emu`` with all dependent conda (and pip) packages.
The installation folder (for configuration files etc) is by default ``~/birdhouse``.
Configuration options can be overriden in the buildout ``custom.cfg`` file. The ``ANACONDA_HOME`` and ``CONDA_ENVS_DIR`` locations
can be changed in the ``Makefile.config`` file.

Now, check out the emu code from GitHub and start the installation:

.. code-block:: sh

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu
   $ make clean install

After successful installation you need to start the services:

.. code-block:: sh

   $ make start  # starts supervisor services
   $ make status # shows supervisor status

The depolyed WPS service is by default available on http://localhost:8094/wps?service=WPS&version=1.0.0&request=GetCapabilities.

Check the log files for errors:

.. code-block:: sh

   $ tail -f  ~/birdhouse/var/log/pywps/emu.log
   $ tail -f  ~/birdhouse/var/log/supervisor/emu.log

You will find more information about the installation in the `Makefile documentation <http://birdhousebuilderbootstrap.readthedocs.io/en/latest/>`_.

Run Emu as Docker container
---------------------------

Emu WPS is available as docker image. You can download the docker image from `DockerHub <https://hub.docker.com/r/birdhouse/emu/>`_
or build it from the provided Dockerfile.

Use `docker-compose <https://docs.docker.com/compose/install/>`_ (you need a recent version > 1.7) to start the container:

.. code-block:: sh

    $ docker-compose up

By default the WPS is available on port 8080: http://localhost:8080/wps?service=WPS&version=1.0.0&request=GetCapabilities.

You can change the ports and hostname with environment variables:

.. code-block:: sh

    $ HOSTNAME=emu HTTP_PORT=8094 SUPERVISOR_PORT=48094 docker-compose up

Now the WPS is available on port 8094: http://emu:8094/wps?service=WPS&version=1.0.0&request=GetCapabilities.

You can also customize the ``docker-compose.yml`` file.
See the `docker-compose documentation <https://docs.docker.com/compose/environment-variables/>`_.
