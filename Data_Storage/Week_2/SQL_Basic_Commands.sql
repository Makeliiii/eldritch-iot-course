CREATE TABLE countries(
    country_id INT PRIMARY KEY NOT NULL,
    country_name VARCHAR(40),
    region_id DECIMAL(10,0),
);

INSERT INTO countries(country_name) 
VALUES
    ('finland'),
    ('canada'),
    ('norway'),
    ('switzerland'),
    ('uganda');

UPDATE countries SET country_name = "N/A" WHERE country_name = NULL;

UPDATE employees SET email = "not available";

UPDATE employees SET email = "not available" WHERE department_id = 80 and commission_pct < 0.20;

ALTER TABLE locations ADD region_id DECIMAL(10,0);

ALTER TABLE locations DROP COLUMN city;

ALTER TABLE locations ADD PRIMARY KEY (location_id);