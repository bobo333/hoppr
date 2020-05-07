#! /usr/bin/env bash

docker run -d \
    --name hoppr_postgres \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_DB=hoppr \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -p 5432:5432 \
    -v /home/steve/code/hoppr/db_data:/var/lib/postgresql/data \
    postgres:12.2
