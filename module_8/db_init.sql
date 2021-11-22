-- Ryan Songcuan
-- 11/22/21
-- Module 8.2 Assignment

-- drop test user if exists
DROP USER IF EXISTS 'pysports_user'@'localhost';

-- create pysports_user and grant them all priveleges to the pysports database
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'csd-310';

-- grant all privileges to the pysports database to user pysports_user on localhost
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';

-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

-- create the team table
CREATE TABLE team (
	team_id		INT				NOT NULL	AUTO_INCREMENT,
	team_name	VARCHAR(75)		NOT NULL,
	mascot		VARCHAR(75)		NOT NULL,
	PRIMARY KEY(team_id)
);

-- create the player table and set the foreign key
CREATE TABLE player (
	player_id	INT				NOT NULL	AUTO_INCREMENT,
	first_name	VARCHAR(75)		NOT NULL,
	last_name	VARCHAR(75)		NOT NULL,
	team_id		INT				NOT NULL,
	PRIMARY KEY(player_id),
	CONSTRAINT fk_team
	FOREIGN KEY (team_id)
	REFERENCES team(team_id)
);

-- insert team records
INSERT INTO team(team_name, mascot)
	VALUES('Team Gryffindor', 'Lions');
INSERT INTO team(team_name, mascot)
	VALUES('Team Slytherin', 'Snakes');

-- insert player records
INSERT INTO player(first_name, last_name, team_id)
	VALUES ('Harry', 'Potter', (SELECT team_id FROM team WHERE team_name = 'Team Gryffindor'));
INSERT INTO player(first_name, last_name, team_id)
	VALUES ('Hermione', 'Granger', (SELECT team_id FROM team WHERE team_name = 'Team Gryffindor'));
INSERT INTO player(first_name, last_name, team_id)
	VALUES ('Ron', 'Weasley', (SELECT team_id FROM team WHERE team_name = 'Team Gryffindor'));
INSERT INTO player(first_name, last_name, team_id)
	VALUES ('Draco', 'Malfoy', (SELECT team_id FROM team WHERE team_name = 'Team Slytherin'));
INSERT INTO player(first_name, last_name, team_id)
	VALUES ('Vincent', 'Crabbe', (SELECT team_id FROM team WHERE team_name = 'Team Slytherin'));
INSERT INTO player(first_name, last_name, team_id)
	VALUES ('Gregory', 'Goyle', (SELECT team_id FROM team WHERE team_name = 'Team Slytherin'));

