-- schema.sql

CREATE TABLE countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_country char(3),
    name VARCHAR(100) NOT NULL,
    region VARCHAR(50),
    capital VARCHAR(100),
    population BIGINT,

    UNIQUE KEY uq_country_name (name)
);