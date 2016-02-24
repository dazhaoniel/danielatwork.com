drop table if exists dp_entries;

create table dp_entries (
  id integer primary key autoincrement,
  name string not null,
  url string not null,
  year string not null,
  image_url string not null,
  description string not null,
  created timestamp not null,
  last_updated timestamp not null
  );