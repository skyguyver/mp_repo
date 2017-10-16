# mp_repo

postgres:
docker run -d -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin --name mp_db -p 5433:5432 --restart=always postgres:9.6

odoo:
docker run -v /mp_repo/trunk:/mnt/extra-addons  -p 8070:8069 --name malphil --link mp_db:db -it odoo:10

pgadmin4:
docker run --name pgadmin4 --link postgres9.6:postgres -p 5050:5050 -d fenglc/pgadmin4