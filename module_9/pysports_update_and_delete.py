# Ryan Songcuan
# 12/5/21
# Module 9.3 Assignment - PySports: Updates & Deletes

import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "pysports_user",
	"password": "csd-310",
	"host": "127.0.0.1",
	"database": "pysports",
	"raise_on_warnings": True
}

try:
	db = mysql.connector.connect(**config)

	print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

	input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print(" The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print(" The specified database does not exist")

	else:
		print(err)

cursor = db.cursor()
cursor.execute("""INSERT INTO player(first_name, last_name, team_id)
	VALUES ('Severus', 'Snape', (SELECT team_id FROM team WHERE team_name = 'Team Gryffindor'));""")
cursor.execute("""SELECT player_id, first_name, last_name, team_name
	FROM player
	INNER JOIN team
		ON player.team_id = team.team_id;""")
players = cursor.fetchall()
print("- - DISPLAYING PLAYERs AFTER INSERT - -")
for player in players:
	print("Player ID: {}".format(player[0]))
	print("First Name: {}".format(player[1]))
	print("Last Name:{}".format(player[2]))
	print("Team Name: {}\n".format(player[3]))

input("\n\n Press any key to continue...")

cursor.execute("""UPDATE player
	SET team_id = 2
	WHERE first_name = "Severus";""")
cursor.execute("""SELECT player_id, first_name, last_name, team_name
	FROM player
	INNER JOIN team
		ON player.team_id = team.team_id;""")
players = cursor.fetchall()
print("- - DISPLAYING PLAYERS AFTER UPDATE - -")
for player in players:
	print("Player ID: {}".format(player[0]))
	print("First Name: {}".format(player[1]))
	print("Last Name:{}".format(player[2]))
	print("Team Name: {}\n".format(player[3]))

input("\n\n Press any key to continue...")

cursor.execute("""DELETE FROM player
	WHERE first_name = "Severus";""")
cursor.execute("""SELECT player_id, first_name, last_name, team_name
	FROM player
	INNER JOIN team
		ON player.team_id = team.team_id;""")
players = cursor.fetchall()
print("- - DISPLAYING PLAYERS AFTER DELETE - -")
for player in players:
	print("Player ID: {}".format(player[0]))
	print("First Name: {}".format(player[1]))
	print("Last Name:{}".format(player[2]))
	print("Team Name: {}\n".format(player[3]))

input("\n\n Press any key to continue...")


db.close()



