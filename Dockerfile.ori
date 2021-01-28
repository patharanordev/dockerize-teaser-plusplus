FROM nvidia/cuda:10.0-runtime-ubuntu18.04 

LABEL maintainer="Nick Rubell" 
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.version="1.0"
LABEL org.label-schema.description="An example to to setup working image, ready to use Tensorflow 2 and Anaconda pacakges." 
LABEL org.label-schema.url="http://blog.rubell.com/how-to-install-anaconda-tensorflow-2-gpu-in-docker-on-ubuntu"
LABEL org.label-schema.docker.cmd="docker run --gpus all -v src:/root/shared:ro -it anaconda-tensorflow2-gpu:latest" 

#*******************************************
#
# Image Arguments and Environment Variables 
#
#*******************************************

# Specifies where Anaconda will be installed.
ENV CONDA_PATH=/opt/anaconda3

# Specifies the environment name to use.
ENV ENVIRONMENT_NAME=main

#*******************************************
#
# General initializations 
#
#*******************************************

# Set default shell to bash for this session.
# By default CUDA image uses dash (/bin/sh -> dash) 
SHELL ["/bin/bash", "-c"]

#*******************************************
#
# Install CuDNN 
#
#*******************************************

# Install CuDNN.
COPY ./aux/libcudnn7_7.6.3.30-1+cuda10.0_amd64.deb /tmp
RUN dpkg -i /tmp/libcudnn7_7.6.3.30-1+cuda10.0_amd64.deb

#*******************************************
#
# Install and Prepare Anaconda 
#
#*******************************************

# curl is required to download Anaconda.
RUN apt-get update && apt-get install curl -y

# Download and install Anaconda.
RUN cd /tmp && curl -O https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
RUN chmod +x /tmp/Anaconda3-2019.07-Linux-x86_64.sh
RUN mkdir /root/.conda
RUN bash -c "/tmp/Anaconda3-2019.07-Linux-x86_64.sh -b -p ${CONDA_PATH}"

# Initializes Conda for shell interaction.
RUN ${CONDA_PATH}/bin/conda init bash

# Upgrade Conda to the latest version
RUN ${CONDA_PATH}/bin/conda update -n base -c defaults conda -y

# Create the working environment and setup its activation on start.
RUN ${CONDA_PATH}/bin/conda create --name ${ENVIRONMENT_NAME} -y
RUN echo conda activate ${ENVIRONMENT_NAME} >> /root/.bashrc

#*******************************************
#
# Install packages from environment.yml 
#
#*******************************************

# Copy environment.yml to /tmp
COPY ./environment.yml /tmp/

# This statement illustrates how to install packages using environment.yml on image creation.

# Update the working environment if USE_ENVIRONMENT_FILE is true.
RUN . ${CONDA_PATH}/bin/activate ${ENVIRONMENT_NAME} \
  && conda env update --file /tmp/environment.yml --prune

#*******************************************
#
# Final Preparations
#
#*******************************************

# Copy the test script. Use it to verify if GPU is enabled after the container is started.
COPY ./test-gpu.py /root

#*******************************************
#
# Clean up the Image
#
#*******************************************

RUN rm -rf /tmp/*
