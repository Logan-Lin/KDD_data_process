create table bj_current_aq
(
	stationid varchar(128) not null,
	utctime datetime not null,
	`PM2.5` int null,
	PM10 int null,
	NO2 int null,
	CO double null,
	O3 int null,
	SO2 int null,
	primary key (stationid, utctime)
)
engine=InnoDB
;
