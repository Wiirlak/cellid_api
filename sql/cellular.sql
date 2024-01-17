CREATE TABLE cellular (
  `radio`			VARCHAR(255) NOT NULL,
  `mcc`				INTEGER,
  `net`				INTEGER,
  `area`			INTEGER,
  `cell`			INTEGER,
  `unit`			FLOAT,
  `longitude`		FLOAT,
  `latitude`		FLOAT,
  `cell_range`		INTEGER,
  `samples`			INTEGER,
  `changeable`		INTEGER,
  `created`			TIMESTAMP,
  `updated`			TIMESTAMP,
  `average_signal`	INTEGER,
  `geom`            GEOMETRY(POINT, 4326),
  PRIMARY KEY (`radio`, `mcc`, `net`, `area`)
 );

