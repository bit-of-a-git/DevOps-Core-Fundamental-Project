FROM mysql:5.7
# Add a database and root password
ENV MYSQL_DATABASE=library
ENV MYSQL_ROOT_PASSWORD=password
#All scripts copied to docker-entrypoint-initdb.d/ are automatically
# executed during container startup
COPY . docker-entrypoint-initdb.d/
