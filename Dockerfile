# vim:set ft=dockerfile:
FROM birdhouse/bird-base:latest
MAINTAINER https://github.com/bird-house/emu

LABEL Description="Emu Web Processing Service Application" Vendor="Birdhouse" Version="0.2.1"

# Configure hostname and user for services 
ENV HOSTNAME localhost
ENV USER www-data
ENV OUTPUT_PORT 8090


# Set current home
ENV HOME /root

# Load sources from github
RUN mkdir -p /opt/birdhouse && curl -ksL https://github.com/bird-house/emu/archive/master.tar.gz | tar -xzC /opt/birdhouse --strip-components=1

# cd into application
WORKDIR /opt/birdhouse



# Install system dependencies
RUN bash bootstrap.sh -i && bash requirements.sh

# Set conda enviroment
ENV ANACONDA_HOME /opt/conda
ENV CONDA_ENVS_DIR /opt/conda/envs

# Run install
RUN make clean install 

# Volume for data, cache, logfiles, ...
RUN chown -R $USER $CONDA_ENVS_DIR/birdhouse
RUN mv $CONDA_ENVS_DIR/birdhouse/var /data && ln -s /data $CONDA_ENVS_DIR/birdhouse/var
VOLUME /data/cache
VOLUME /data/lib

# Ports used in birdhouse
EXPOSE 8094 28094 $OUTPUT_PORT

# Start supervisor in foreground
ENV DAEMON_OPTS --nodaemon --user $USER

# Start service ...
CMD ['make', 'update-config', 'start']

