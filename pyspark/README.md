# Spark

## Setup with Docker

<pre># run 
docker-compose up -d
# retrieve containerId of master
docker ps | grep master
# run jupyter notebook
docker exec -it ContainerIdMaster jupyter notebook --log-level=INFO --allow-root
# stop docker
docker-compose down
</pre

The password to authenticate in Jupyter is _*jupyter*_