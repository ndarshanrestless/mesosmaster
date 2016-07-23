DROP TABLE IF EXISTS registered_mesos;
DROP TABLE IF EXISTS docker_container_data;
CREATE TABLE registered_mesos
(
  ip TEXT PRIMARY KEY,
  id_name TEXT
);


/* create another table with dockerid (text), mesosslaveid(text), mesosmasterid(text) */ 
CREATE TABLE docker_container_data
(
  docker_id TEXT,
  mesos_slave_id TEXT,
  mesos_master_id TEXT
);
