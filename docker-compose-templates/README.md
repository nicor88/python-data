# Run different DBs with Docker

## MySQL
<pre>
docker-compose -f docker-compose-templates/docker-mysql.yml up
</pre>

## PostgresDB
<pre>
docker-compose -f docker-compose-templates/docker-postgres.yml up
</pre>

## CleanUP
<pre>
# Stop all the containers
docker stop $(docker ps -a -q)
# Remove all the containers
docker rm $(docker ps -a -q)
# Remove all the images
docker rmi $(docker images -a -q)
</pre>