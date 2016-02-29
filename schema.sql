DROP TABLE if exists "dp_entries";
CREATE TABLE "dp_entries" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" varchar(39) NOT NULL,
  "url" varchar(39) NOT NULL,
  "year" varchar(39) NOT NULL, 
  "image_url" varchar(39) NOT NULL,
  "description" varchar(256) NOT NULL,
  "created" timestamp NOT NULL, 
  "last_updated" timestamp NOT NULL
  );

DROP TABLE if exists "dp_stack";
CREATE TABLE "dp_stack" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "project" integer NOT NULL REFERENCES dp_entries(id),
  "name" varchar(39) NOT NULL
  );