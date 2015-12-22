# vim:set ft=dockerfile:
FROM birdhouse/bird-base:latest
MAINTAINER https://github.com/bird-house/emu

LABEL Description="Emu Web Processing Service Application" Vendor="Birdhouse" Version="0.2.1"

# Configure hostname and user for services 
ENV HOSTNAME localhost
ENV USER www-data
ENV OUTPUT_PORT 38094


# Set current home
ENV HOME /root

# Copy application sources
COPY . /opt/birdhouse

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
RUN mkdir /data && mv $CONDA_ENVS_DIR/birdhouse/var/lib /data && ln -s /data/lib $CONDA_ENVS_DIR/birdhouse/var
VOLUME /data

# Ports used in birdhouse
EXPOSE 8094 28094 $OUTPUT_PORT

# Start supervisor in foreground
ENV DAEMON_OPTS --nodaemon --user $USER

# Start service ...
CMD ["make", "update-config", "start"]

