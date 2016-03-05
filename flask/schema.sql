DROP TABLE if exists `dp_entries`;
CREATE TABLE `dp_entries` (
  `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT, # in wordpress
  `name` varchar(39) NOT NULL, # in wordpress
  `url` varchar(39) NOT NULL,
  `year` varchar(39) NOT NULL, 
  `image_url` varchar(39) NOT NULL,
  `description` varchar(256) NOT NULL, # in wordpress
  `created` timestamp NOT NULL, # in wordpress
  `last_updated` timestamp NOT NULL # in wordpress
  );

DROP TABLE if exists `dp_stack`;
CREATE TABLE `dp_stack` (
  `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  `project` integer NOT NULL REFERENCES dp_entries(id),
  `name` varchar(39) NOT NULL
  );