CREATE DATABASE IF NOT EXISTS dev;

USE dev;

CREATE TABLE contas (
    id integer not null auto_increment,
    username varchar(100),
    password varchar(100),
    email varchar(100),
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;