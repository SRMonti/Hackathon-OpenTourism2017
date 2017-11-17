drop table if exists entries;
create table map (
  id varchar(20) not null unique primary key,
  reated datetime not null,  -- set by server DEFAULT now()
  center_lat real not null,          -- -90.00000..90.00000
  center_lon real not null,           -- -180.00000..180.00000
  zoom int not null           -- level 8..18
);

create table marker (
  id int primary key,
  map_id int not null references map,
  comment varchar(255) null,
  lat real not null,          -- -90.00000..90.00000
  lon real not null           -- -180.00000..180.00000
);
