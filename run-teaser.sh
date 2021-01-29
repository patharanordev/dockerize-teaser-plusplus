docker run -d --gpus all \
-p "8888:8888" \
-v notebook:/app/notebook \
--restart always \
--name=cuda-jupyter-conda \
patharanor/teasor-pp:0.0.5