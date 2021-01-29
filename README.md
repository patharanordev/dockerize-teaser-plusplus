# How to setup Anaconda and Tensorflow 2 for local development in Docker in Ubuntu

This is the source code for the following article:

https://blog.rubell.com/how-to-install-anaconda-tensorflow-2-gpu-in-docker-on-ubuntu

## Running by building and running container manually

Follow the [Build and Test the Image](https://blog.rubell.com/how-to-install-anaconda-tensorflow-2-gpu-in-docker-on-ubuntu/#build-and-test-the-image) steps described in the article.

Run JupyterLab

```bash
$ docker run --gpus all \
patharanor/cuda-conda-jupyter:0.0.1 \
/opt/anaconda3/bin/conda install -c conda-forge jupyterlab && \
jupyter lab --port=8890 --no-browser --ip=0.0.0.0 --allow-root
```