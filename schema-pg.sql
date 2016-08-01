DROP TABLE IF EXISTS register_master_table;
DROP TABLE IF EXISTS register_slave_table;
DROP TABLE IF EXISTS docker_container_table;
/*Creating a table for the master ip and id*/
CREATE TABLE register_master_table
(
  master_ip TEXT ,
  master_id TEXT PRIMARY KEY
);

/*Creating a table for the slave id*/
CREATE TABLE register_slave_table
(
  slave_ip TEXT ,
  slave_id TEXT PRIMARY KEY,
  master_id TEXT REFERENCES register_master_table(master_id)
);

/*Creating a table for docker containers*/
CREATE TABLE docker_container_table
(
  docker_container_id TEXT ,
  docker_container_status TEXT,
  slave_id TEXT REFERENCES register_slave_table(slave_id)
);

