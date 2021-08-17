
DROP TABLE regions;
DROP TABLE munros;


CREATE TABLE regions (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255)  
);

CREATE TABLE munros (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    height VARCHAR(255),
    climbed BOOLEAN,
    region_id INT REFERENCES regions(id)
);
