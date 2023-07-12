
CREATE DATABASE IF NOT EXISTS population;

USE population;


drop table if exists people;
drop table if exists places;

CREATE TABLE places (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    county VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    INDEX idx_city (city)
);

CREATE TABLE people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    given_name VARCHAR(255) NOT NULL,
    family_name VARCHAR(255) NOT NULL,
    date_of_birth DATE,
    place_of_birth VARCHAR(255),
    FOREIGN KEY (place_of_birth) REFERENCES places(city)
);