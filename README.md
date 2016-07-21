Master to talk to mesos master 

Setup Database:
 psql -h localhost -d bar -U bar -W bar -a -f schema-pg.sql


API end points are:

http://54.84.252.49:5000/registermaster?mesos_server_ip=54.84.252.123&docker_id=120743&mesos_server_name=nidhi-lapyy-meso-server

http://54.84.252.49:5000/dockerdeath?docker_id=120743&mesos_server_ip=54.84.252.123