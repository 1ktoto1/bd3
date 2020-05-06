CREATE TABLE Author (
    name VARCHAR(128) NOT NULL PRIMARY KEY,
    country VARCHAR(70) NOT NULL,
    url VARCHAR(256) NOT NULL
);

CREATE TABLE Country (
    country varchar(70) NOT NULL PRIMARY KEY
    );

ALTER TABLE Author
add constraint country_fk FOREIGN KEY (country) REFERENCES Country (country); 

CREATE TABLE Game (
    game VARCHAR(128) NOT NULL PRIMARY KEY
    );

CREATE TABLE Map (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    game VARCHAR(128) NOT NULL,
    rating INT NOT NULL,
    author_name VARCHAR(128) NOT NULL,
    downloads INT NOT NULL,
    map_date DATE NOT NULL
);

ALTER TABLE Map
ADD CONSTRAINT author_name_fk FOREIGN KEY (author_name) REFERENCES Author (name);

ALTER TABLE Map
ADD CONSTRAINT game_fk FOREIGN KEY (game) REFERENCES Game (game);